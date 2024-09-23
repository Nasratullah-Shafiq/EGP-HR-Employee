# -*- coding: utf-8 -*-
from odoo import fields, models, api

class EmployeeDistrict(models.Model):
    _name = 'employee.district'
    _description = 'Employee district'

    province = fields.Many2one('egp.procurement.province', string='Province')
    district = fields.Many2one('egp.procurement.district', string='District', domain="[('id', 'in', avialable_district_ids)]")

    avialable_district_ids = fields.Many2many('egp.procurement.district', compute='_compute_avialable_district')

    @api.depends('province')
    def _compute_avialable_district(self):
        for rec in self:
            rec.avialable_district_ids = rec.province.district_ids