# -*- coding:utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import Warning

class Rooms(models.Model):
	_name = "rooms"
	_description = "Rooms"

	room_id = fields.Many2one("room.reservation","Room")
	room_name = fields.Many2one("room.name","Room Name")
	room_status = fields.Selection("Status",related='room_name.status')
	room_price = fields.Float("Price",related='room_name.price')
	room_capacity = fields.Integer("Capacity",related='room_name.capacity')

	