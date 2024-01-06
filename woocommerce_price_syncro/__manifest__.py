{
    "name": "Woocommerce Price Syncro",
    "summary": "Syncro price from woocommerce to odoo",
    "version": "16.0.1.0.0",
    "category": "Custom",
    "author": "Xtendoo",
    "license": "LGPL-3",
    "application": True,
    "depends": [
        "base",
        "woo_commerce_ept",
    ],
    "data": [
        "views/product_product_view.xml",
    ],
    "installable": True,
}
