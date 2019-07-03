# -*- coding:utf-8 -*-

from odoo import models, fields, api, _

class One2manyField(models.Model):
    _name = "one.2.many.field"
    _description = "One 2 many"

    name = fields.Char("Name")
    partner_id = fields.One2many("many.2.one.field","partner","Categories")
