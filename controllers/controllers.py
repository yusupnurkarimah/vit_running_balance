# -*- coding: utf-8 -*-
from odoo import http

# class VitRunningBalance(http.Controller):
#     @http.route('/vit_running_balance/vit_running_balance/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_running_balance/vit_running_balance/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_running_balance.listing', {
#             'root': '/vit_running_balance/vit_running_balance',
#             'objects': http.request.env['vit_running_balance.vit_running_balance'].search([]),
#         })

#     @http.route('/vit_running_balance/vit_running_balance/objects/<model("vit_running_balance.vit_running_balance"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_running_balance.object', {
#             'object': obj
#         })