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
from odoo.osv import expression
import ast


class LoyaltyRule(models.Model):
    _inherit = 'loyalty.rule'

    condition_type = fields.Selection([('and', 'AND'), ('or', 'OR')], 'Condition type', default='or', required=True)
    product_value_ids = fields.Many2many('product.attribute.value', 'loyalty_rule_product_attribute_value_rel',
                                         'rule_id', 'value_id', 'Product Attributes')
    brand_ids = fields.Many2many('product.brand', 'loyalty_rule_product_brand_rel', 'rule_id', 'brand_id', 'Brand')
    family_ids = fields.Many2many('product.family', 'loyalty_rule_product_family_rel', 'rule_id', 'family_id', 'Families')

    def _get_valid_product_domain(self):
        self.ensure_one()
        domain = super(LoyaltyRule, self)._get_valid_product_domain()
        if self.condition_type == 'or':
            operator = expression.OR
        else:
            operator = expression.AND
        product_domain = []
        if self.product_value_ids:
            product_domain = operator([product_domain,
                               [('product_template_variant_value_ids.product_attribute_value_id', '=', v.id) for v in
                                self.product_value_ids]])
        if self.family_ids:
            product_domain = operator([product_domain, [('product_family_id', 'in', self.family_ids.ids)]])
        if self.brand_ids:
            product_domain = operator([product_domain, [('product_brand_id', 'in', self.brand_ids.ids)]])
        return expression.AND([domain, product_domain])
