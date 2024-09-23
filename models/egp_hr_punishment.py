# -*- coding: utf-8 -*-
from odoo import fields, models, api


class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'
    _description = "Human Resource"

    punishment_ids = fields.One2many('employee.punishment', 'employee_id', string='Punishment')


# Your Python code (e.g., in a controller or model)

class EmployeePunishment(models.Model):
    _name = 'employee.punishment'
    _description = 'Employee punishment'

    employee_id = fields.Many2one('hr.employee', string='Employee')

    punishment_type = fields.Char(string='Punishment Type')
    violation_type = fields.Char(string='Violation Type')
    order = fields.Char(string='Order')

    punishment_start_date = fields.Date(string='Start Date')
    punishment_end_date = fields.Date(string='End Date')
    punishment_date = fields.Date(string='Date Of Punishment')
    # invalid = fields.Char(string='Invalid')
    # invalid = fields.Selection([('invalid', 'Invalid')], string="Invalid")
    # invalid = fields.Boolean(string='Invalid')
    punishment_remarks = fields.Char(string='Remarks')








