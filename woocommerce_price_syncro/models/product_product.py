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
                 ('compute_price', '=', 'fixed')],
                limit=1,
            )
            if list_price:
                product.write({
                    'list_price': list_price.fixed_price,
                    'barcode': list_price.default_code,
                })

# 5q8a-4saf-aqac
