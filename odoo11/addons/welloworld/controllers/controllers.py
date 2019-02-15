# -*- coding: utf-8 -*-
from odoo import http

# class Welloworld(http.Controller):
#     @http.route('/welloworld/welloworld/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/welloworld/welloworld/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('welloworld.listing', {
#             'root': '/welloworld/welloworld',
#             'objects': http.request.env['welloworld.welloworld'].search([]),
#         })

#     @http.route('/welloworld/welloworld/objects/<model("welloworld.welloworld"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('welloworld.object', {
#             'object': obj
#         })