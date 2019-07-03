# -*- coding:utf-8 -*-

from odoo import models, fields, api, _

class Many2ManyField(models.Model):
    _name = "many.2.many.field"
    _description = "Many 2 many"

    name = fields.Char("Name")
    web_id = fields.Many2many("res.partner","partner","record_id","partner_id","Web name")
