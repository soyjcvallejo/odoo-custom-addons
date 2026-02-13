# Copyright 2026 Open Support
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)

{
    "name": "Product Label ZPL 2x1",
    "summary": "Generates 2x1 inch ZPL product labels, with optional price display, using a wizard and QWeb-text reports.",
    "version": "18.0.1.0.0",
    "development_status": "Alpha",
    "category": "Inventory/Inventory",
    "website": "https://github.com/soyjcvallejo/odoo-custom-addons",
    "author": "Open Support",
    "maintainers": ["soyjcvallejo"],
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "product",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/product_label_templates.xml",
        "views/report_product_label_zpl_2x1.xml",
        "views/report_product_label_zpl_2x1_price.xml",
    ],
}
