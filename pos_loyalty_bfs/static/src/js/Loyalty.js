/** @odoo-module **/

import {Order, Orderline, PosGlobalState} from 'point_of_sale.models';
import Registries from 'point_of_sale.Registries';

const BFSOrderline = (Orderline) => class BFSOrderline extends Orderline {
    _getSpecificDiscountableLines(reward) {
        const discountableLines = [];
        const applicableProducts = reward.all_discount_product_ids;
        for (const line of this.get_orderlines()) {
            if (!line.get_quantity()) {
                continue;
            }
            if (applicableProducts.has(line.get_product().id) ||
                applicableProducts.has(line.reward_product_id || 0)) {
                discountableLines.push(line);
            }
        }
        return discountableLines;
    }
};

Registries.Component.extend(Orderline, BFSOrderline);
