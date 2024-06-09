# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class odoo_training(models.Model):
#     _name = 'odoo_training.odoo_training'
#     _description = 'odoo_training.odoo_training'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


from odoo import models, fields, api
from odoo.exceptions import ValidationError
from random import randint
from datetime import timedelta


class TrainingCourse(models.Model):
    _name = 'training.course'
    _description = 'Training Kursus'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    def get_default_color(self):
        return randint(1, 11)

    name = fields.Char(string='Judul', required=True, tracking=True)
    description = fields.Text(string='Keterangan', tracking=True)
    user_id = fields.Many2one('res.users', string="Penanggung Jawab", default=lambda self: self.env.uid, tracking=True)
    session_line = fields.One2many('training.session', 'course_id', string='Sesi', tracking=True)
    product_ids = fields.Many2many(
        'product.product',
        'course_product_rel',
        'course_id',
        'product_id',
        'Cendera Mata',
        tracking=True)
    ref = fields.Char(string='Referensi', readonly=True, default='/')
    level = fields.Selection([('basic', 'Dasar'), ('advanced', 'Lanjutan')], string='Tingkatan', default='basic')
    color = fields.Integer('Warna', default=get_default_color)
    email = fields.Char(string="Email", related='user_id.login')

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('training.course')
        return super(TrainingCourse, self).create(vals)


class TrainingSession(models.Model):
    _name = 'training.session'
    _description = 'Training Sesi'
    _sql_constraints = [
        ('nama_kursus_unik', 'UNIQUE(name)', 'Judul kursus harus unik'),
        ('nama_keterangan_cek', 'CHECK(name != description)', 'Judul kursus dan keterangan tidak boleh sama')
    ]

    def default_partner_id(self):
        instruktur = self.env['res.partner'].search([('instructor', '=', True)], limit=1)
        return instruktur

    @api.depends('seats', 'attendee_ids')
    def compute_taken_seats(self):
        for sesi in self:
            sesi.taken_seats = 0
            if sesi.seats and sesi.attendee_ids:
                sesi.taken_seats = 100 * len(sesi.attendee_ids) / sesi.seats

    @api.depends('start_date', 'duration')
    def get_end_date(self):
        for sesi in self:
            if not sesi.start_date:
                sesi.end_date = sesi.start_date
                continue

            start = fields.Date.from_string(sesi.start_date)
            sesi.end_date = start + timedelta(days=sesi.duration - 1)

    def set_end_date(self):
        for sesi in self:
            if not (sesi.start_date and sesi.end_date):
                continue

            start_date = fields.Datetime.from_string(sesi.start_date)
            end_date = fields.Datetime.from_string(sesi.end_date)
            sesi.duration = (end_date - start_date).days + 1

    course_id = fields.Many2one('training.course', string='Judul Kursus', required=True, ondelete='cascade')
    name = fields.Char(string='Nama', required=True)
    start_date = fields.Date(string='Tanggal')
    duration = fields.Float(string='Durasi', help='Jumlah Hari Training', default=1)
    seats = fields.Integer(string='Kursi', help='Jumlah Kuota Kursi')
    partner_id = fields.Many2one(
        'res.partner',
        string='Instruktur',
        domain=[('instructor', '=', True)],
        default=default_partner_id)
    email = fields.Char(related='partner_id.email', string='Email')
    attendee_ids = fields.Many2many(
        'training.attendee',
        'session_attendee_rel',
        'session_id',
        'attendee_id',
        'Peserta')
    taken_seats = fields.Float(string='Kursi Terisi', compute='compute_taken_seats')
    end_date = fields.Date(string="Tanggal Selesai", compute='get_end_date', inverse='set_end_date', store=True)
    attendees_count = fields.Integer(string="Jumlah Peserta", compute='get_attendees_count', store=True)
    color = fields.Integer('Color Index', default=0)
    level = fields.Selection(string='Tingkatan', related='course_id.level')
    state = fields.Selection(
        [('draft', 'Draft'), ('open', 'Open'), ('done', 'Done')],
        string='Status',
        readonly=True,
        default='draft')

    @api.depends('attendee_ids')
    def get_attendees_count(self):
        for sesi in self:
            sesi.attendees_count = len(sesi.attendee_ids)

    @api.constrains('seats', 'attendee_ids')
    def check_seats_and_attendees(self):
        for r in self:
            if r.seats < len(r.attendee_ids):
                raise ValidationError('Jumlah peserta melebihi kuota yang disediakan')

    @api.onchange('duration')
    def verify_valid_duration(self):
        if self.duration <= 0:
            self.duration = 1
            raise ValidationError('Durasi Hari Training Tidak Boleh 0 atau Negatif')
            # return {
            #     'warning': {
            #         'title': 'Perhatian',
            #         'message': 'Durasi Hari Training Tidak Boleh 0 atau Negatif'
            #     }
            # }

    def action_confirm(self):
        self.write({'state': 'open'})

    def action_cancel(self):
        self.write({'state': 'draft'})

    def action_close(self):
        self.write({'state': 'done'})

    def cron_expire_session(self):
        now = fields.Date.now()
        expired_ids = self.search([('end_date', '<', now), ('state', '=', 'open')])
        expired_ids.write({'state': 'done'})

    def action_print_session(self):
        return self.env.ref('odoo_training.report_training_session_action').report_action(self)


class TrainingAttendee(models.Model):
    _name = 'training.attendee'
    _description = 'Training Peserta'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner', 'Partner', required=True, ondelete='cascade')
    gender = fields.Selection([('male', 'Pria'), ('female', 'Wanita')], string='Gender',
                              required=True, help='Jenis Kelamin')
    marital = fields.Selection([
        ('single', 'Belum Menikah'),
        ('married', 'Menikah'),
        ('divorced', 'Cerai')],
        string='Pernikahan', help='Status Pernikahan')
    session_ids = fields.Many2many('training.session', 'session_attendee_rel', 'attendee_id',
                                   'session_id', 'Sesi')
