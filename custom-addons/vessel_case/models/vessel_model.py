# -*- coding: utf-8 -*-

from odoo import models, fields


class Vessel(models.Model):
    _name = 'vessel.vessel'
    _description = 'Vessel'

    name = fields.Char(string='Vessel Name', required=True)
    vessel_type = fields.Selection(
        [('klm', 'KLM'), ('barge', 'Barge'), ('tugboat', 'Tugboat'), ('kapal_tangker', 'Kapal Tangker'),
         ('roro', 'Roro')],
        'Vessel Type',
        required=True)
    call_sign = fields.Char(string='Call Sign', required=True)
    imo_number = fields.Char(string='IMO Number', required=True)
    mmssi_number = fields.Char(string='MMSSI Number', required=True)
    year_build = fields.Date(string='Year Build', required=True)
    grt = fields.Char(string='GRT', required=True)
    dwt = fields.Char(string='DWT', required=True)
    loa = fields.Char(string='LOA', required=True)
    propeller_type = fields.Char(string='Propeller Type', required=True)
    main_engine = fields.Char(string='Main Engine', required=True)
    aux_engine = fields.Char(string='AUX Engine', required=True)
    aux_engine2 = fields.Char(string='AUX Engine 2')
    aux_engine3 = fields.Char(string='AUX Engine 3')


class Room(models.Model):
    _name = 'vessel.room'
    _description = 'Vessel Room'

    name = fields.Char(string='Room Name', required=True)
    vessel_id = fields.Many2one('vessel.vessel', string='Vessel Name', required=True)
    parent_room = fields.Selection([
        ('BRIDGE', 'BRIDGE'), ('ENGINE_ROOM', 'ENGINE ROOM'), ('CONTROL_ROOM', 'CONTROL ROOM'),
        ('MAP_ROOM', 'MAP ROOM')], 'Parent Room')
    description = fields.Text(string='Description', required=True)
