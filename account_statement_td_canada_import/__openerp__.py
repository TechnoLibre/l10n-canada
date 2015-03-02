# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2014 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
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
    'name': 'Account Statement TD Canada Import',
    'version': '0.1',
    'author': "Savoir-faire Linux,Odoo Community Association (OCA)",
    'maintainer': 'Savoir-faire Linux',
    'website': 'http://www.savoirfairelinux.com',
    'license': 'AGPL-3',
    'category': 'Finance',
    'summary': 'TD Canada CSV statement import',
    'description': """
This module allows importing bank statements downloaded from the
TD Canada website in the CSV format.

Contributors
------------
* Marc Cassuto (marc.cassuto@savoirfairelinux.com)
* Maxime Chambreuil (maxime.chambreuil@savoirfairelinux.com)
* Savoir-faire Linux (support@savoirfairelinux.com)
* Vincent Vinet (vincent.vinet@savoirfairelinux.com)
""",
    'depends': [
        'account_statement_base_import',
    ],
    'external_dependencies': {
        'python': [],
    },
    'data': [
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}
