from odoo import api, fields, models

class Buyproducts(models.Model):
    _name = "products_cat.buy_product"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "buy products"



    customer_id = fields.Many2one('products_cat.customers', string='Customer')
    customer_email = fields.Char(related='customer_id.email', string="Email")
    customer_phone = fields.Integer(related='customer_id.phone', string="Phone")
    customer_address = fields.Char(related='customer_id.address', string="Address")

    product_id = fields.Many2one('products_cat.myproduct', string='Product')
    product_quantity = fields.Integer(string='Quantity' ,default=1)
    product_price = fields.Float(related='product_id.price' ,string="Unit Price")

    # all_detail = fields.Many2one('products_cat.myproduct','product_all' ,string='products_all')

    all_detail = fields.One2many('products_cat.buy_product','products_ids' ,string='order_products')

    state = fields.Selection([
        ('add to cart', 'Add To Cart'),
        ('proceed to checkout', 'Proceed To Checkout'),
        ('payment', 'Payment')
    ] , default='add to cart' , string='Status' , required=True)


    #
    # @api.depends('name')
    # def compute_change_quantity(self):
    #
    #     if self.user_has_groups('product_cat.group_product_cat_inventory_manager'):
    #         self.readonly_quant = True
    #         print('Found')
    #     else:
    #         print('Not found')
    #         self.readonly_quant = False


class Orders(models.Model):
    _name = "products_cat.buy_product"

    products_all_id = fields.Many2one("products_cat.myproduct")
    products_all_price = fields.Float(related='products_all_id.price')
    products_ids= fields.Many2one("products_cat.buy_product", string="Products_allls")

