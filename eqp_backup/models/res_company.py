# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    eqp_backup_enable_local = fields.Boolean(
        string='Activate Local Functionality',
        help="This policy will activate the Local Backup functionality.")
    eqp_backup_enable_sftp = fields.Boolean(
        string='Activate SFTP Functionality',
        help="This policy will activate the Secure File Transfer Protocol (SFTP) transfer functionality.")
    eqp_backup_enable_drive = fields.Boolean(
        string='Activate Google Drive Functionality',
        help="This policy will activate the Google Drive transfer functionality.")
    eqp_backup_enable_dropbox = fields.Boolean(
        string='Activate Dropbox Functionality',
        help="This policy will activate the Dropbox transfer functionality.")

    eqp_backup_enable_success_email = fields.Boolean(
        string='Activate Success Email Notification',
        help="This policy activates automatic email notifications upon successful completion of a backup process.")
    eqp_backup_enable_failure_email = fields.Boolean(
        string='Activate Failure Email Notification',
        help="This policy activates automatic email notifications upon failure of a backup process.")

    eqp_backup_success_email_address = fields.Char(
        string='Additional email addresses for Success Notifications',
        help="By default, the system sends notifications to the responsible user of the backup record. However, "
             "here you can add additional email addresses for notification if needed.")
    eqp_backup_failure_email_address = fields.Char(
        string='Additional email addresses for Failure Notifications',
        help="By default, the system sends notifications to the responsible user of the backup record. However, "
             "here you can add additional email addresses for notification if needed.")

    backup_master_password = fields.Char(
        string='Database Management Master Password',
        help="This field stores the hash of the Database Master Password upon confirmation and authentication. "
             "It is utilized by the backup module during the automated backup process execution.")
