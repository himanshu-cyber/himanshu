# -*- coding:utf-8 -*-

from odoo import models, fields, api, _

class Many2OneField(models.Model):
    _name = "many.2.one.field"
    _description = "Many 2 One"

    name = fields.Char("Name")
    partner = fields.Many2one("one.2.many.field","Partner")
