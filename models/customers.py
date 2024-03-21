from odoo import api, fields, models

class Customers(models.Model):
    _name = "products_cat.customers"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Customer"

    name = fields.Char( string='Name')
    address = fields.Char( string='Address')
    phone = fields.Integer(string="Phone")
    email = fields.Char(string="Email")

