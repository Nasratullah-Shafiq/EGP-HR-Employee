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

    punishment_type = fields.Selection([
        ('removal_of_duty_job', 'Removal of Duty Job'),
        ('removal_of_current_rank', 'Removal of Current Rank'),
        ('fine', 'Fine'),
        ('salary_deduction', 'Salary Deduction'),
        ('dismissal_of_duty', 'Dismissal of Duty'),
        ('recommendation', 'Recommendation'),
        ('warning', 'Warning'),
        ('change_of_duty', 'Change of Duty'),
        ('contract_cancelled', 'Contract Cancelled')], string="Punishment Type")

    violation_type = fields.Selection([
        ('uniform', 'Uniform'),
        ('educational', 'Educational'),
        ('behavioral', 'Behavioral'),
        ('administrative', 'Administrative'),
        ('traffics', 'Traffics'),
        ('holiday', 'Holiday'),
        ('religious affairs', 'Religious ََAffairs'),
        ('missing_card', 'Missing Card'),
        ('murder', 'Murder')], string="Violation Type")

    order = fields.Char(string='Order')

    punishment_start_date = fields.Date(string='Start Date')
    punishment_end_date = fields.Date(string='End Date')
    punishment_date = fields.Date(string='Date Of Punishment')

    punishment_remarks = fields.Char(string='Remarks')








