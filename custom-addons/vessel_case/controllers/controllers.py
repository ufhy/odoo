# -*- coding: utf-8 -*-
# from odoo import http


# class VesselCase(http.Controller):
#     @http.route('/vessel_case/vessel_case', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vessel_case/vessel_case/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vessel_case.listing', {
#             'root': '/vessel_case/vessel_case',
#             'objects': http.request.env['vessel_case.vessel_case'].search([]),
#         })

#     @http.route('/vessel_case/vessel_case/objects/<model("vessel_case.vessel_case"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vessel_case.object', {
#             'object': obj
#         })

