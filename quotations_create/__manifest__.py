# -*- coding: utf-8 -*-

{
    'name':'quotation_create',
    'description': 'Quotation',
    'summary': 'Quotation',
    'category': 'Quotation',
    'version': '12.0.0.0.0',
    'author': 'Silent Solutions Pvt.Ltd.',
    'wedsite': 'https://www.silentsolution.com',
    'depends':[
        'sale',
        'base',
        'product'
    ],
    'data':[
        'security/ir.model.access.csv',
        'views/quotations_info_view.xml',
        'views/menu_view.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
