# -*- coding:utf-8 -*-

from odoo import models, fields, api, _

class Services(models.Model):
	_name = "services"
	_description = "Room Services"

	services_id = fields.Many2one('room.reservation','Services')
	name = fields.Char("Name")
	list_price = fields.Float("Services Rant")
	categ_id = fields.Many2one("services.type","Services Category")
	product = fields.Many2one('services','Product')
	services_price = fields.Float('Services Price',related='product.list_price')