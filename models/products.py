from odoo import api, fields, models

class Category(models.Model):
    _name = 'products_cat.category'
    _description = 'Product Category'


    name = fields.Char(string='Name')
    description = fields.Text(string='Description')

class Products(models.Model):
    _name = "products_cat.myproduct"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "products"
    _rec_name = 'name'



    name = fields.Char(string='Name' )
    price = fields.Float(string='Price', default=0)
    quantity = fields.Integer( string='Quantity',default=1 )
    size = fields.Selection([('s', 'S'), ('l', 'L'),('xl', 'XL'),('xxl', 'XXL')], string='Size')
    image = fields.Image(string='Product Image')
    category_id = fields.Many2one('products_cat.category', string='Category')
    readonly_quant = fields.Boolean(string='Quant' ,compute="compute_change_quantity")
    # product_all = fields.One2many("products_cat.buy_product",string="product_all")
    # order_products= fields.Many2one("products_cat.buy_product",string='order products')

    @api.depends('name')
    def compute_change_quantity(self):

        if self.user_has_groups('product_cat.group_product_cat_inventory_manager'):
            self.readonly_quant = True
            print('Found')
        else:
            print('Not found')
            self.readonly_quant = False
