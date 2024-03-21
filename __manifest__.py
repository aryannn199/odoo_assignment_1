# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Product_Catalog',
    'version': '1.0.0',
    'category': 'product_cat',
    'sequence':-100,
    'summary': '',
    'description': """ """,
    'depends': ['base', 'mail'],
    'author': 'aryan',
    'data': [
        "security/ir.model.access.csv",
        "security/security.xml",
        "views/menu.xml",
        "views/products_view.xml",
        "views/buy_product_view.xml",
        "views/customers_view.xml",

    ],
    'demo': [],
    'installable': True,
    'application': True,
    'sequence': "-100",
    'assets': {},
    'post_init_hook': '',
    'license': 'LGPL-3',
}
