# -*- coding: utf-8 -*-
{
    'name': "OWL Tutorial",
    'summary': """
       OWL Tutorial""",
    'description': """
        OWL Tutorial
    """,
    'sequence': '-700',
    'author': "Abrus",
    'website': "http://www.abrusnetworks.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'OWL',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    'installable':True,
    'application':True,
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/todo_list.xml'
    ],
    'assets':{
        'web.assets_backend':[
            'owl/static/src/components/*/*.js',
            'owl/static/src/components/*/*.xml',
            'owl/static/src/components/*/*.scss',
        ],
    },
}
