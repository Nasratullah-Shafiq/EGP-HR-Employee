# -*- coding: utf-8 -*-
from odoo import fields, models, api

class EgpHrInherit(models.Model):
    _inherit = 'hr.employee'
    _description = "Human Resource"

    training_ids = fields.One2many('employee.training', 'employee_id', string='Training')

# Your Python code (e.g., in a controller or model)

class EmployeeTraining(models.Model):
    _name = 'employee.training'
    _description = 'Employee Training'

    employee_id = fields.Many2one('hr.employee', string='Employee')

    course_id = fields.Many2one('employee.course', string="Training Type", tracking=True)
    training_location = fields.Char(string='Training Location')
    training_start_date = fields.Date(string='Start Date')
    training_end_date = fields.Date(string='End Date')
    training_result = fields.Selection([('supreme', 'Supreme'), ('Excellent', 'Excellent'), ('Good', 'Good'),
                                        ('medium', 'medium'), ('elementary', 'elementary')], string="Training Result")
    training_certification = fields.Char(string='Certification')
    training_remarks = fields.Char(string='Remarks')


class EmployeeCourse(models.Model):
    _name = 'employee.course'
    _description = 'Employee Course'

    name = fields.Char(string='Course')



























