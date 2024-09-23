# -*- coding: utf-8 -*-
from odoo import fields, models, api


class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'
    _description = "Human Resource"

    retirement_ids = fields.One2many('employee.retirement', 'employee_id', string='Retirement')


# Your Python code (e.g., in a controller or model)

class EmployeeRetirement(models.Model):
    _name = 'employee.retirement'
    _description = 'Employee Retirement'

    employee_id = fields.Many2one('hr.employee', string='Employee')

    retirement_type_id = fields.Many2one('employee.retirement.type', string="Retirement Type")
    retirement_reason_id = fields.Many2one('employee.retirement.reason', string="Retirement Reason")
    retirement_end_date = fields.Date(string='End Date')
    retirement_remarks = fields.Char(string='Remarks')



class EmployeeRetirementReason(models.Model):
    _name = 'employee.retirement.reason'
    _description = 'Employee Reason'

    name = fields.Char(string='Reason')

class EmployeeRetirementType(models.Model):
    _name = 'employee.retirement.type'
    _description = 'Employee Retirement Type'

    name = fields.Char(string='Retirement Type')




