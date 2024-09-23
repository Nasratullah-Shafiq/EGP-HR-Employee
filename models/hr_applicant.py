# -*- coding: utf-8 -*-
from odoo import fields, models, api


class HrEmployeeInherit(models.Model):
    _inherit = 'hr.applicant'
    _description = "Human Resource"
