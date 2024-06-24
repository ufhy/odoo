# -*- coding: utf-8 -*-

from odoo import models, fields


class Task(models.Model):
    _name = 'vessel.task'
    _description = 'Task'

    name = fields.Char(string='Task Name', required=True)
    job_id = fields.Many2one('vessel.job', string='Job Name', required=True)


class TaskLine(models.Model):
    _name = 'vessel.taskline'
    _description = 'Task Line'

    product_id = fields.Many2one('product.product', string='Product Name', required=True)
