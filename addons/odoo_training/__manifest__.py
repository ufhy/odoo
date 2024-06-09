# -*- coding: utf-8 -*-
{
    'name': "odoo_training",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Pelatihan',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'mail'],

    # always loaded
    'data': [
        'report/report_training_session.xml',
        'report/report_action.xml',
        'data/data.xml',
        'data/sequence_data.xml',
        'data/scheduler_data.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/training_views.xml',
        'views/training_attendee_views.xml',
        'views/session_views.xml',
        'views/partner_views.xml',
        'wizard/training_wizard_views.xml',
        'views/menuitem_views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
}
