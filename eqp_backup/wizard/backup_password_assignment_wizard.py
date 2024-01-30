# -*- coding: utf-8 -*-
##############################################################################
#
#    EQP Solutions
#
#    Copyright (C) 2024-TODAY EQP Solutions (<https://www.eqpsolutions.com>)
#    Author: EQP Solutions (<info@eqpsolutions.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import api, fields, models, _
from odoo.tools import config
from odoo.exceptions import UserError, ValidationError, AccessDenied


class BackupPasswordAssignmentWizard(models.TransientModel):
    """
    Wizard for assigning the Backup Master Password in the configuration settings.

    This wizard allows users with the 'EQP Automatic Backups / Admin' role to validate and set the Backup Master Password.
    The entered password is verified against the Database Management Master Password, and upon successful validation,
    it is stored in the 'backup_master_password' field of the corresponding 'res.config.settings' record.
    """
    _name = 'backup.password.assignment.wizard'
    _description = 'Backup Password Assignment'

    backup_password = fields.Char(string='Master Password',
                                  help='Please input the Master Password here for validation and secure storage.')

    def validate_master_password(self):
        """
        Validates the entered Master Password and sets it in the 'backup_master_password' field of 'res.config.settings'.

        :return: Action to close the wizard if successful.
        :rtype: dict
        """
        if self.user_has_groups("eqp_backup.group_eqp_backup_admin"):
            password = self.backup_password

            if password and config.verify_admin_password(password):
                active_model = self.env.context.get('active_model')
                active_id = self.env.context.get('active_id')

                if active_model == 'res.config.settings' and active_id:
                    res_config = self.env[active_model].browse(active_id)

                    if res_config:
                        hash_password = config.options['admin_passwd']
                        res_config.write({'backup_master_password': hash_password})
                        return {'type': 'ir.actions.act_window_close'}
                    else:
                        raise ValidationError("No record found for the provided ID in res.config.settings.")
                else:
                    raise ValidationError("This action is only applicable for 'res.config.settings'.")
            else:
                raise AccessDenied()
        else:
            raise UserError(
                "To set the backup password, you must have the 'EQP Automatic Backups / Admin' role. "
                "If you don't have this role, kindly request assistance from someone with the necessary "
                "permissions to execute this action."
            )
