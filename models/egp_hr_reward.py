# -*- coding: utf-8 -*-
from odoo import fields, models, api


class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'
    _description = "Human Resource"

    reward_ids = fields.One2many('employee.reward', 'employee_id', string='reward')


# Your Python code (e.g., in a controller or model)

class EmployeeReward(models.Model):
    _name = 'employee.reward'
    _description = 'Employee Reward'

    employee_id = fields.Many2one('hr.employee', string='Employee')
    reward_type = fields.Selection([('sign', 'Sign'), ('medal', 'Medal'), ('cash', 'Cash'),
                                    ('one_month_salary', 'One Month Salary'),
                                    ('honorary_letter_of_appreciation', 'Honorary Letter of Appreciation'),
                                    ('encouragement_of_civil_services_workers', 'Encouragement of civil service workers'),
                                    ('first_degree_of_appreciation', 'First degree of appreciation'),
                                    ('second_degree_of_appreciation', 'Second degree of appreciation'),
                                    ('third_degree_of_appreciation', 'Third degree of appreciation')],
                                   string="Reward Type", default='medal')
    amount_of_cash_for_reward = fields.Integer(string='Amount of Cash for Reward')
    order_no = fields.Integer(string='Order No')
    order_date = fields.Date(string='Order Date')
    organization_id = fields.Many2one('employee.organization', string="Appreciation of the Organization")
    reason = fields.Char(string='Reason')









