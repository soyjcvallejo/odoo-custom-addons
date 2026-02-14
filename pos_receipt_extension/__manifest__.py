# Copyright 2026 Open Support
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)

{
    "name": "POS Receipt Extension",
    "summary": "Extends the default POS receipt layout",
    "version": "18.0.1.0.0",
    "development_status": "Alpha",
    "category": "Sales/Point of Sale",
    "website": "https://github.com/soyjcvallejo/odoo-custom-addons",
    "author": "Open Support",
    "maintainers": ["soyjcvallejo"],
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "auto_install": False,
    "depends": [
        "point_of_sale",
    ],
    "assets": {
        "point_of_sale._assets_pos": [
            "pos_receipt_extension/static/src/xml/pos_receipt_extension.xml",
            "pos_receipt_extension/static/src/js/pos_receipt_extension.js",
        ],
    },
}
