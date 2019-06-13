# -*- coding: utf-8 -*-

{
    'name': 'Tranning',
    'description': 'Tranning odoo',
    'summary': 'Tranning',
    'category': 'Tranning',
    'version': '12.0.0.0.0',
    'author': 'Silent Solutions Pvt. Ltd.',
    'website': 'https://www.silentsolution.com',
    'depends': [
        'sale',
        'base',
        'product'
    ],
    'data': [
        'views/menu_view.xml',
        'security/ir.model.access.csv',
        'views/room_reservation_view.xml',
        'data/data.xml',
        'views/room_name_view.xml',
        'views/room_type_view.xml',
        'views/services_view.xml',
        'views/services_type_view.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}

