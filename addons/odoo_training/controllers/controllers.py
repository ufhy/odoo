# -*- coding: utf-8 -*-
# from odoo import http


# class OdooTraining(http.Controller):
#     @http.route('/odoo_training/odoo_training', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_training/odoo_training/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_training.listing', {
#             'root': '/odoo_training/odoo_training',
#             'objects': http.request.env['odoo_training.odoo_training'].search([]),
#         })

#     @http.route('/odoo_training/odoo_training/objects/<model("odoo_training.odoo_training"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_training.object', {
#             'object': obj
#         })

