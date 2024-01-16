# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api, tools


class ProductProduct(models.Model):
    _inherit = 'product.product'

    reduced_price = fields.Float(
        string='Reduced Price',
        default=0.0,
        digits='Product Price',
        groups="base.group_user",
        help="The price at which the product is sold on the sales channels.",
    )

    def action_woocommerce_price_syncro(self):
        pricelist_sale = self.env['product.pricelist'].search(
            [('name', '=', 'Woo https://aryentto.es')],
            limit=1,
        )
        pricelist_reduced = self.env['product.pricelist'].search(
            [('name', '=', 'Woo https://aryentto.es Sale Pricelist')],
            limit=1,
        )

        for product in self:
            if product.barcode != product.default_code:
                product.default_code = product.barcode

            if pricelist_sale:
                list_prices = self.env['product.pricelist.item'].search(
                    [('pricelist_id', '=', pricelist_sale.id),
                     ('product_id', '=', product.id),
                     ('applied_on', '=', '0_product_variant'),
                     ('compute_price', '=', 'fixed'),
                     ('fixed_price', '>', 0)],
                )
                if list_prices:
                    list_price = list_prices.sorted(key=lambda r: r.fixed_price)[0]
                    product.list_price = list_price.fixed_price

            if pricelist_reduced:
                list_prices = self.env['product.pricelist.item'].search(
                    [('pricelist_id', '=', pricelist_reduced.id),
                     ('product_id', '=', product.id),
                     ('applied_on', '=', '0_product_variant'),
                     ('compute_price', '=', 'fixed'),
                     ('fixed_price', '>', 0)],
                )
                if list_prices:
                    list_price = list_prices.sorted(key=lambda r: r.fixed_price)[0]
                    product.reduced_price = list_price.fixed_price

    def create(self, vals):
        product = super(ProductProduct, self).create(vals)
        print("create"*10)
        return product
