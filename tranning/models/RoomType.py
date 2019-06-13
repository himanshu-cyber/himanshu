# -*- coding:utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import Warning

class RoomType(models.Model):
	_name = "room.type"
	_description = "Room Type"

	
	name = fields.Char("Name")