# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Canadian Check Writing',
    'version': '1.0',
    'author': "Savoir-faire Linux,Odoo Community Association (OCA)",
    'website': 'http://www.savoirfairelinux.com',
    'category': 'Generic Modules/Accounting',
    'description': """
Print checks in Canadian's format'
==================================

This module provides reports to print check using the canadian format from:
http://www.cdnpay.ca/imis15/pdf/pdfs_rules/standard_006_fr.pdf

    """,
    'depends': ['account_check_writing'],
    'data': [
        'l10n_ca_account_check_writing_report.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'active': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
