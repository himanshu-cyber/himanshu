# -*- coding: utf-8 -*-

{
    'name': 'Relection Field',
    'description': 'Relection Field',
    'summary': 'Relection Field',
    'category': 'Relection Field',
    'version': '12.0.0.0.0',
    'author': 'Silent Solutions Pvt. Ltd.',
    'website': 'https://www.silentsolution.com',
    'depends': [
        'sale',
        'base',
        'product'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/Many2onefield_view.xml',
        'views/One2manyfield_view.xml',
        'views/Many2manyfield_view.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
