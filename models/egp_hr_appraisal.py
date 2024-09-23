# -*- coding: utf-8 -*-
from odoo import fields, models, api


class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'
    _description = "Human Resource"

    appraisal_ids = fields.One2many('employee.appraisal', 'employee_id', string='Appraisal')


# Your Python code (e.g., in a controller or model)

class EmployeeAppraisal(models.Model):
    _name = 'employee.appraisal'
    _description = 'Employee Appraisal'

    employee_id = fields.Many2one('hr.employee', string='Employee')

    appraisal_type = fields.Selection([('trail', 'Trail'), ('annual', 'Annual'), ('monthly', 'Monthly'),
                                       ('trail_according_to_the_plan', 'Trail According To The Plan'),
                             ('quarterly', 'Quarterly')], string="Appraisal Type", default='annual')
    total_marks = fields.Integer(string='Total Marks')
    head_details = fields.Selection([('head', 'Head'), ('external_head', 'External Head'), ('superior_head', 'Superior Head'),
                                       ('supervisor', 'Supervisor'),
                                       ('quarterly', 'Quarterly')], string="Head Details", default='superior_head')
    sending_date = fields.Date(string='Sending Date')
    basic_objective_of_work_plan = fields.Selection([('yes', 'Yes'), ('no', 'No')],
                                                    string="Basic objective of work plan", default='yes')
    head_opinion = fields.Char(string='Head Opinion')
    superior_head_opinion = fields.Char(string='Superior Head')
    appraisal_date = fields.Date(string='Appraisal Date')
    is_action_plan_accommodated = fields.Selection([('yes', 'Yes'), ('no', 'No')], string="Action Plan Accommodation",
                                                   default='yes')
    final_result = fields.Selection([('2nd_step', 'Upgrade to the Second step'),
                                     ('3rd_step', 'Upgrade to the Third step'),
                                     ('4th_step', 'Upgrade to the Fourth step'),
                                     ('5th_step', 'Upgrade to the Fifth step'),
                                     ('conversion_to_province', 'Discipline (conversion to provinces)'),
                ('continuation_position', 'Continuation of duty in the current position'),
                ('job_announcement', 'Job Announcement'),
                ('introduce_to_capacity_building', 'Continuation of duty in active duties and steps and introduction to education')],
                                    string="Final Result", default='2nd_step')
    employee_opinion = fields.Char(string='Employee Opinion')
    is_agree_with_the_result = fields.Selection([('yes', 'Yes'), ('no', 'No')], string="Agree with the result",
                                                   default='yes')
    admin_opinion = fields.Char(string='Admin Opinion')
    employee_opinion_again = fields.Char(string='Employee Opinion')
    supervisor_opinion = fields.Char(string='Superior Head')

