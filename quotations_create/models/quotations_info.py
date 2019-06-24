# -*- coding:utf-8 -*-


from odoo import models, fields, api, _

class QuotationsInfo(models.Model):
    _name = "quotations.info"
    _description = "Quotations Information"

    partner_id = fields.Many2one("res.partner","Customer")
    suppler_id = fields.Many2one("res.partner","Suppler")
    # crm_ids = fields.One2many("crm.lead","quotation_inquiry","Suppler")
    product_ids = fields.One2many("quotations.info.line","quotation_id","Product")
    price_subtotal = fields.Float("SubTotal")
    product_total = fields.Float("Total Amount",compute="compute_product_total",store=True)

    @api.multi
    @api.depends('product_ids','price_subtotal')
    def compute_product_total(self):
        for record in self:
            record.product_total = sum(record.product_ids.mapped('price_subtotal')) or 0


class QuotationsInfoLine(models.Model):
    _name = "quotations.info.line"
    _description = "Quotations Line"

    quotation_id = fields.Many2one("quotations.info")
    product_id = fields.Many2one("product.product", "Product")
    product_qty = fields.Float("Ordered Qty")
    price_unit = fields.Float("Unit Price",related="product_id.lst_price")
    price_subtotal = fields.Float("Subtotal", compute="compute_qty_total",store=True)


    @api.multi
    @api.depends('product_qty','price_unit')
    def compute_qty_total(self):
        for record in self:
            record.price_subtotal = record.product_qty * record.price_unit
