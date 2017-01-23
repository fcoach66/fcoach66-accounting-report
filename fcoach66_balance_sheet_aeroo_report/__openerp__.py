# -*- coding: utf-8 -*-

{
    'name': 'Balance sheet report',
    'version': '8.0.1.0.0',
    'author': 'fcoach66',
    'category': 'Accounting',
    'summary': 'Balance sheet report',
    'website': '',
    'depends': [
        'fcoach66_asset_account',
        'fcoach66_liablity_account',
        'report_aeroo',
        ],
    'data': [
        'wizards/wizard_balance_sheet.xml',
        'reports/report_balance_sheet_ods.xml',
        'reports/report_balance_sheet_xls.xml',
        ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'AGPL-3',
}
