# -*- coding: utf-8 -*-

{
    'name': 'Qwed Report Sale Order',
    'description': 'Qwed Report odoo',
    'summary': 'Qwed',
    'category': 'Qwed',
    'version': '12.0.0.0.0',
    'author': 'Silent Solutions Pvt. Ltd.',
    'website': 'https://www.silentsolution.com',
    'depends': [
        'sale'
    ],
    'data': [
        'report_views/qwed_report_sale_order.xml',
        'report_views/qwed_report_sale_report_templates.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
