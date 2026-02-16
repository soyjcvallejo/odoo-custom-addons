from odoo import models, fields

class ProductLabelLayout(models.TransientModel):
    _inherit = 'product.label.layout'

    print_format = fields.Selection(
        selection_add=[
            ('zpl_2x1', 'Etiquetas ZPL 2x1 pulgadas'),
            ('zpl_2x1_price', 'Etiquetas ZPL 2x1 pulgadas - con precio'),
            ('zpl_2x1_barcode-4x1', 'Etiquetas ZPL 2x1 pulgadas - 4 códigos de barras (CODE 18)'),
        ],
        ondelete={
            'zpl_2x1': 'set default',
            'zpl_2x1_price': 'set default',
            'zpl_2x1_barcode-4x1': 'set default',
        }
    )

    def process(self):
        self.ensure_one()

        if self.print_format == 'zpl_2x1':
            report_action = self.env.ref(
                'product_label_zpl_2x1.action_report_label_zpl_2x1'
            ).report_action(self.product_ids)
            report_action['context'] = dict(report_action.get('context', {}))
            report_action['context'].update({'custom_quantity': self.custom_quantity or 1})
            report_action.update({'close_on_report_download': True})
            return report_action

        if self.print_format == 'zpl_2x1_price':
            report_action = self.env.ref(
                'product_label_zpl_2x1.action_report_label_zpl_2x1_price'
            ).report_action(self.product_ids)
            report_action['context'] = dict(report_action.get('context', {}))
            report_action['context'].update({'custom_quantity': self.custom_quantity or 1})
            report_action.update({'close_on_report_download': True})
            return report_action
        
        if self.print_format == 'zpl_2x1_barcode-4x1':
            report_action = self.env.ref(
                'product_label_zpl_2x1.action_report_label_zpl_2x1_barcode-4x1'
            ).report_action(self.product_ids)
            report_action['context'] = dict(report_action.get('context', {}))
            report_action['context'].update({'custom_quantity': self.custom_quantity or 1})
            report_action.update({'close_on_report_download': True})
            return report_action

        return super().process()

