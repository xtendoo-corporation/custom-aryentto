# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api, tools


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def action_woocommerce_price_syncro(self):
        for product in self:
            list_price = self.env['product.pricelist.item'].search(
                [('product_id', '=', product.id),
                 ('applied_on', '=', '0_product_variant'),
                 ('compute_price', '=', 'fixed'),
                 ('fixed_price', '>', 0)],
            )
            if list_price:
                fixed_price = list_price.sorted(key=lambda r: r.fixed_price)[0]
                product.write({
                    'list_price': fixed_price,
                    'barcode': product.default_code,
                })

