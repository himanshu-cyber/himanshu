# -*- coding:utf-8 -*-

from odoo import models, fields, api, _

class ServicesType(models.Model):
	_name = "services.type"
	_description = "Services Type"

	name = fields.Char("Services Name")