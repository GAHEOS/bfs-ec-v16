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
from odoo.exceptions import ValidationError, UserError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    height = fields.Float('Height', compute='_compute_dimension_height', inverse='_set_dimension_height',
                          store=True)
    width = fields.Float('Width', compute='_compute_dimension_width', inverse='_set_dimension_width', store=True)
    depth = fields.Float('Width', compute='_compute_dimension_depth', inverse='_set_dimension_depth', store=True)

    @api.depends('product_variant_ids', 'product_variant_ids.depth')
    def _compute_dimension_depth(self):
        unique_variants = self.filtered(lambda tmpl: len(tmpl.product_variant_ids) == 1)
        for template in unique_variants:
            template.depth = template.product_variant_ids.depth
        for template in (self - unique_variants):
            template.depth = False

    def _set_dimension_depth(self):
        for template in self:
            if len(template.product_variant_ids) == 1:
                template.product_variant_ids.depth = template.depth

    @api.depends('product_variant_ids', 'product_variant_ids.width')
    def _compute_dimension_width(self):
        unique_variants = self.filtered(lambda tmpl: len(tmpl.product_variant_ids) == 1)
        for template in unique_variants:
            template.width = template.product_variant_ids.width
        for template in (self - unique_variants):
            template.width = False

    def _set_dimension_width(self):
        for template in self:
            if len(template.product_variant_ids) == 1:
                template.product_variant_ids.width = template.width

    @api.depends('product_variant_ids', 'product_variant_ids.height')
    def _compute_dimension_height(self):
        unique_variants = self.filtered(lambda tmpl: len(tmpl.product_variant_ids) == 1)
        for template in unique_variants:
            template.height = template.product_variant_ids.height
        for template in (self - unique_variants):
            template.height = False

    def _set_dimension_height(self):
        for template in self:
            if len(template.product_variant_ids) == 1:
                template.product_variant_ids.height = template.height

    @api.onchange('height', 'width', 'depth')
    def _onchange_dimensions(self):
        self.volume = self.height * self.width * self.depth


class ProductProduct(models.Model):
    _inherit = 'product.product'

    height = fields.Float('Height', digits='Height')
    width = fields.Float('Width', digits='Height')
    depth = fields.Float('Depth', digits='Depth')
    volume = fields.Float('Volume', digits='Volume', compute='_compute_volume', store=True, readonly=True)

    @api.depends('height', 'width', 'depth')
    def _compute_volume(self):
        for rec in self:
            rec.volume = rec.height * rec.width * rec.depth
