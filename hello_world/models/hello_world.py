# Copyright 2026 Open Support
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0)

from odoo import models, fields


class HelloWorld(models.Model):
    _name = "hello.world"
    _description = "Hello World Model"

    name = fields.Char(
        string="Name",
        required=True,
    )

    message = fields.Text(
        string="Message",
    )

    active = fields.Boolean(
        default=True,
    )
