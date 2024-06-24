# -*- coding: utf-8 -*-

from odoo import models, fields


class Job(models.Model):
    _name = 'vessel.job'
    _description = 'Vessel Job'

    name = fields.Char(string='Job Name', required=True)
    job_type = fields.Selection(
        [('Preventive_Maintenance', 'Preventive Maintenance'), ('Corrective_Maintenance', 'Corrective Maintenance')],
        string='Job Type', required=True)
