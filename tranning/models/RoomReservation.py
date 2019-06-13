# -*- coding:utf-8 -*-

import re
from datetime import *
from dateutil.relativedelta import *
from odoo import models, fields, api, _
from odoo.exceptions import Warning

class RoomReservation(models.Model):
	_name = "room.reservation"
	_description = "Room Reservation"

	booking_no = fields.Char("Booking Number")
	name = fields.Many2one("res.partner","Name")
	street = fields.Char("Street")
	street2 = fields.Char("Street2")
	city = fields.Char("City")
	country_id = fields.Many2one('res.country','Country')
	state_id = fields.Many2one('res.country.state', 'State', domain="[('country_id', '=', country_id)]")
	email = fields.Char("Email")
	num_child = fields.Integer("Child")
	num_adults = fields.Integer("Adults")
	contact = fields.Char("Contact",context={'code','=',country_id})
	check_in = fields.Datetime('Check In')
	check_out = fields.Datetime('Check Out')
	num_of_days = fields.Integer("Number Of Days")
	room_price = fields.Float("Room Price")
	services_price = fields.Float("Services Price")
	total_person = fields.Integer("Total Persons", compute='_compute_total')
	is_mail = fields.Boolean("Mail")
	rooms_id = fields.One2many('rooms','room_id','Rooms')
	services_ids = fields.One2many('services','services_id','Services')
	rooms_total = fields.Float("Total Amount Rooms", compute='_compute_room_price')
	services_total = fields.Float("Total Amount Services", compute='_compute_services_price')
	amount_total = fields.Float("Total", compute='_compute_total_amount')

	@api.multi
	@api.depends('num_child','num_adults')
	def _compute_total(self):
		for each in self:
			each.total_person = each.num_child + each.num_adults

	# @api.onchange('check_in')
	# def _onchange_check_in(self):
	# 	if self.check_in:
	# 		d1 = datetime.strptime(self.check_in,"%Y-%m-%d %H:%M:%S").date()
	# 		d2 = date.today()
	# 		if d1 < d2:
	# 			raise Warning(_('Invalid Date'))
	# 		else:
	# 			self.check_out = d1 + relativedelta(days=self.num_of_days)

	@api.constrains('email')
	def _constrains(self):
		if self.email:
			match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
			if match == None:
				raise Warning(_('Pleace Enter your valid email address'))

	@api.constrains('contact')
	def _check_phone_number(self):
		match = re.compile("^[0-9]{10}$")
		res = self.contact.split('-')
		if match.match(res[1]) and len(res[1]) == 10:
			return True
		else:
			raise Warning(_("Pleace Enter your valid Contact number"))

	@api.onchange('country_id')
	def onchange_country_id(self):
		self.contact = str(self.country_id.phone_code)+ '-' if self.country_id else ''

	@api.multi
	@api.depends('rooms_id','room_price')
	def _compute_room_price(self):
		for each in self:
			each.rooms_total = sum(each.rooms_id.mapped('room_price')) or 0

	@api.multi
	@api.depends('services_ids','services_price')
	def _compute_services_price(self):
		for each in self:
			each.services_total = sum(each.services_ids.mapped('services_price')) or 0

	@api.multi
	@api.depends('rooms_total','services_total')
	def _compute_total_amount(self):
		for each in self:
			each.amount_total = each.rooms_total + each.services_total