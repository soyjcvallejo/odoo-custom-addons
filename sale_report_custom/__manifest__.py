# Copyright 2026 Open Support
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0)

{
    "name": "Sale Report Custom",
    "summary": "Extend Sale Order PDF report layout",
    "version": "19.0.1.0.0",
    "development_status": "Alpha",
    "category": "Sales",
    "website": "https://github.com/soyjcvallejo/odoo-custom-addons",
    "author": "Open Support",
    "maintainers": ["soyjcvallejo"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "auto_install": False,
    "depends": [
        "sale",
    ],
    "data": [
        "views/report_saleorder_custom.xml",
    ],
}
