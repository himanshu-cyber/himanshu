# -*- coding:utf-8 -*-

from datetime import datetime
from odoo import models, fields, api, _


class QuotationsInfo(models.Model):
    _name = "quotations.info"
    _description = "Quotations Information"

    vendor_id = fields.Many2one("res.partner", "Vendor")
    date_order = fields.Datetime("Order Date", default=fields.Datetime.now)
    state = fields.Selection([('draft', 'Draft'),
                              ('done', 'Done'),
                              ('cancel', 'Cancelled')], required=True, default='draft')
    product_ids = fields.One2many("quotations.info.line", "quotation_id", "Product")
    price_subtotal = fields.Float("SubTotal")
    product_total = fields.Float("Total Amount", compute="compute_product_total", store=True)
    
    @api.multi
    @api.depends('product_ids', 'price_subtotal')
    def compute_product_total(self):
        for record in self:
            record.product_total = sum(record.product_ids.mapped('price_subtotal')) or 0

    def button_confirm(self):
        print("\n\n----self---", self)
        print("\n\n-----self product value line----",self.product_ids)
        res = []
        print("\n\n---res--",res)
        product_dict = {
            'partner_id':self.vendor_id.id,
        }
        print("\n\n---product_dict----",product_dict)
        produt_lst = [0, 0, {
            'product_id': self.product_ids.product_id.id,
            'name': self.product_ids.description,
            'date_planned': self.product_ids.date_planned,
            'product_qty': self.product_ids.product_qty,
            'product_uom': self.product_ids.product_uom.id,
            'price_unit': self.product_ids.price_unit,
            'price_subtotal': self.product_ids.price_subtotal
        }]
        print("\n\n------product_lst----",produt_lst)
        product_dict['order_line'] = [produt_lst]
        print(product_dict)
        product = self.env['purchase.order'].create(product_dict)
        # print("\n\n---======--====res-------========",res)
        print("\n\n------po1----",product)
        product.button_confirm()
        # for record in self.product_ids:
        #         for data in record:
        #             res.append(data)
        # print("\n\n---res record----",res)
        # product = self.env['purchase.order'].create(product_dict)
        # print("\n\n-----pro------",product)
        self.write({'state': 'done'})

    @api.multi
    def button_cancel(self):
        for res in self:
            res.write({'state': 'cancel'})


class QuotationsInfoLine(models.Model):
    _name = "quotations.info.line"
    _description = "Quotations Line"

    quotation_id = fields.Many2one("quotations.info")
    product_id = fields.Many2one("product.product", "Product")
    description = fields.Text("Description")
    date_planned = fields.Datetime("Scheduled Date")
    vendor_name = fields.Many2one("res.partner", "Suppler")
    product_qty = fields.Float("Ordered Qty")
    price_unit = fields.Float("Unit Price", related="product_id.lst_price")
    product_uom = fields.Many2one('uom.uom', string='Product Unit of Measure', required=True)
    price_subtotal = fields.Float("Subtotal", compute="compute_qty_total", store=True)

    @api.multi
    @api.depends('product_qty', 'price_unit')
    def compute_qty_total(self):
        for record in self:
            record.price_subtotal = record.product_qty * record.price_unit

    @api.onchange('product_id')
    def _onchange_product_id(self):
        print("\n\n---------self-----", self.product_id.name)
        print("\n\n-----product vendor----", self.product_id.variant_seller_ids)
        list = []
        for partner in self.product_id.variant_seller_ids:
            list.append(partner.name.id)
        return {'domain': {'vendor_name': [('id', 'in', list)]}}

