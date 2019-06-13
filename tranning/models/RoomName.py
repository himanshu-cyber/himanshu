# -*- coding:utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import Warning

class RoomName(models.Model):
	_name = "room.name"
	_description = "Room Name"

	name = fields.Char("Room Name")
	status = fields.Selection([('available','Available'),
								('occupied','Occupied')],"Status", default='available')
	categ_id = fields.Many2one("room.type","Room Category")
	price = fields.Float("Price")
	capacity = fields.Integer("Capacity")

	@api.constrains('capacity')
	def check_capacity(self):
		print("\n-------",self)
		for room in self:
			print("\n!!!!!!",self)
			if room.capacity <= 0:
				raise Warning(_("Room Capacity must be more than 0"))