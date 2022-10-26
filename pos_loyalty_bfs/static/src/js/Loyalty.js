odoo.define('pos_loyalty_bfs.loyalty', function (require) {
"use strict";

var {PosGlobalState} = require('point_of_sale.models');
const Registries = require('point_of_sale.Registries');


const BFSLoyaltyGlobalState = (PosGlobalState) => class BFSLoyaltyGlobalState extends PosGlobalState {
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

Registries.Component.extend(PosGlobalState, BFSLoyaltyGlobalState);
});