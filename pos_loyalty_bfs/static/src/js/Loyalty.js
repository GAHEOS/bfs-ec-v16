/** @odoo-module alias=pos_loyalty_bfs.models**/

import { Order } from 'point_of_sale.models';
import Registries from 'point_of_sale.Registries';

const BFSLoyaltyOrder = (Order) => class BFSLoyaltyOrder extends Order {
    //@override
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

Registries.Model.extend(Order, BFSLoyaltyOrder);
