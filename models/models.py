# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class vit_running_balance(models.Model):
#     _name = 'vit_running_balance.vit_running_balance'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
class trx(models.Model):
    _name = 'vit_running_balance.trx'
    _rec_name = 'name'
    _order = 'id asc'

    name = fields.Char("Description")
    date = fields.Datetime(string="Date",)
    debit = fields.Float(string="Debit",)
    credit = fields.Float(string="Credit",)
    balance = fields.Float(compute='_get_balance',
                string="Balance", required=False)

    @api.depends('debit', 'credit')
    def _get_balance(self):
        for record in self.sorted(lambda x: x.id):
            prev = self.search_read([('id', '<', record.id)],
                limit=1, order='date desc')
            prev_balance = prev[0]['balance'] if prev else 0
            record.balance = prev_balance + record.debit - record.credit