# -*- coding: utf-8 -*-

{
    'name': 'Trial Balance Report',
    'version': '8.0.1.0.0',
    'author': 'fcoach66',
    'category': 'Accounting',
    'summary': 'Report Trial Balance Aeroo',
    'website': '',
    'depends': [
        'account_accountant',
        'report_aeroo'
    ],
    'data': [
        'security/ir.model.access.csv',
        'report/report_trial_balance.xml',
        'wizard/wizard_trial_balance.xml',
        'menu_Accounting.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3'
}
