#######################################################################################
#
#    GAHEOS S.A.
#    Copyright (C) 2020-TODAY GAHEOS S.A. (https://www.gaheos.com)
#    Author: Leonardo Gavidia Guerra | @leogavidia
#
#    See LICENSE file for full copyright and licensing details.
#
#######################################################################################

{
    'name': 'PoS Loyalty BFS Customization',
    'version': '16.0.1.7',
    'depends': [
        'pos_loyalty',
        'product_brand',
        'product_family',
    ],
    'author': 'GAHEOS S.A.',
    'description': 'PoS Loyalty BFS Customization',
    'category': 'Sales/Point of Sale',
    'website': "https://www.gaheos.com",
    'data': [
        'views/promo_views.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_loyalty_bfs/static/src/js/Loyalty.js'
        ]
    }
}
