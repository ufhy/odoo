# -*- coding: utf-8 -*-

from odoo import models, fields


class Equipment(models.Model):
    _name = 'vessel.equipment'
    _description = 'Vessel Equipment'

    vessel_id = fields.Many2one('vessel.vessel', string='Vessel Name', required=True)
    room_id = fields.Many2one('vessel.room', string='Room Name', required=True)
    parent_id = fields.Many2one('vessel.equipment', string='Parent Equipment',
                                domain="[('vessel_id', '=', vessel_id), ('room_id', '=', room_id)]")
    name = fields.Char(string='Equipment Name', required=True)
    brand = fields.Char(string='Equipment Brand', required=True)
    type = fields.Char(string='Equipment Type', required=True)
    specification = fields.Text(string='Equipment Specification', required=True)
