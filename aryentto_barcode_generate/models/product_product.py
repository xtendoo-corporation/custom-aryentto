# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api, tools


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def create(self, vals):
        products = super(ProductProduct, self).create(vals)
        for product in products:
            if not product.default_code or not product.barcode:
                code = self.env['ir.sequence'].next_by_code('product.product.barcode.sequence') or '/'
                product.default_code = code
                product.barcode = code
        return products
