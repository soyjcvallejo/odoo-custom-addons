# Copyright 2026 Open Support
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0)

{
    "name": "Hello World",
    "summary": "Demo Hello World compliant with OCA standards.",
    "version": "19.0.1.0.0",
    "development_status": "Alpha",
    "category": "Tools",
    "website": "https://github.com/soyjcvallejo/",
    "author": "Open Support",
    "maintainers": ["soyjcvallejo"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/hello_world_views.xml",
    ],
}
