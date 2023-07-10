# -*- coding: utf-8 -*-
{
    'name': "trip_requisition",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'auto_install': True,
    "installable": True,
    "application": True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'invoice', 'fleet'],

    # always loaded
    'data': [
        # models defination
        'models/models_defination.xml',

        # field definations
        'models/trip_consolidation.xml',
        'models/trip_cost_apportionment.xml',
        'models/trip_requisition_status.xml',
        'models/trip_requisition_line.xml',
        'models/trip_requisition.xml',
        'models/trip_requisition_ext.xml',
        'models/journal_extend.xml',

        # actions
        'actions/server.xml',

        # automated actions
        'automation/set_ratios.xml',


        # security rules
        'security/access.xml',

        # views
        # 'views/templates.xml',
        'views/ui/requisition_views.xml',
        'views/ui/status_views.xml',

        # menu items
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
