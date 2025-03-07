# -*- coding: utf-8 -*-
{
    'name': "Wonderbrands Integration Tests",

    'summary': """Inherits button install method to add integration tests""",

    'description': """
        Module that executes behavioral API and shell tests to verify a module before and after installation.
    """,

    'author': "Wonderbrands",
    'website': "http://www.wonderbrands.co",

    'category': 'Technical',
    'version': '0.0.1',
    'depends': [
        'base'
    ],
    'external_dependencies': {
        'python': [
            'behave'
        ] 
    },
    'installable': True,
    'application': True,

}
