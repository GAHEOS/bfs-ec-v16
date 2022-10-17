#######################################################################################
#
#    GAHEOS S.A.
#    Copyright (C) 2020-TODAY GAHEOS S.A. (https://www.gaheos.com)
#    Author: Leonardo Gavidia Guerra | @leogavidia
#
#    See LICENSE file for full copyright and licensing details.
#
#######################################################################################

from odoo import models, fields, api, _


class ProductFamily(models.Model):
    _name = 'product.family'
    _description = "Product Family"

    name = fields.Char('Family Name', required=True)
    description = fields.Text('Description', translate=True)
    partner_id = fields.Many2one('res.partner', string='Partner',
                                 help='Select a partner for this family if any.', ondelete='restrict')
    logo = fields.Binary('Logo File')
    product_ids = fields.One2many('product.template', 'product_family_id', string='Family Products')
    products_count = fields.Integer(string='Number of products', compute='_get_products_count')

    @api.depends('product_ids')
    def _get_products_count(self):
        self.products_count = len(self.product_ids)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_family_id = fields.Many2one('product.family', string='Family', help='Select a family for this product')
