# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'School Apps',
    'version': '20.0.0',
    'category': 'General',
    'depends' : ['base'],
    'description': """
School Apps.
===============================================

Odoo based school apps.
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/student_views.xml',
        'views/absensi_views.xml',
        ],
    'installable' : True,
    'application': True,
    'author': 'Khelsea M. S.',
    'license': 'LGPL-3',
}
