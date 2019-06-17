# -*- coding:utf-8 -*-

import logging
from odoo import models, fields, api, _
from odoo.exceptions import Warning

_logger = logging.getLogger(__name__)

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
		for room in self:
			_logger.warn("\n\n-----This method is call-----")
			if room.capacity <= 0:
				raise Warning(_("Room Capacity must be more than 0"))