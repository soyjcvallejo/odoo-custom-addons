from odoo import models, fields

class ProductLabelTemplate(models.Model):
    _name = 'product.label.template'
    _description = 'Plantillas de etiquetas de producto'

    name = fields.Char(string='Nombre', required=True)
    report_type = fields.Selection([
        ('qweb-pdf', 'PDF'),
        ('qweb-text', 'ZPL')
    ], default='qweb-text', string='Tipo de reporte')
    report_name = fields.Char(string='Nombre de plantilla QWeb', required=True)
    printer_type = fields.Char(string='Tipo de impresora')

