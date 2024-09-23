# -*- coding: utf-8 -*-
from odoo import fields, models, api


class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'
    _description = "Human Resource"

    education_ids = fields.One2many('employee.education', 'employee_id', string='Education')


# Your Python code (e.g., in a controller or model)

class EmployeeEducation(models.Model):
    _name = 'employee.education'
    _description = 'Employee Education'

    employee_id = fields.Many2one('hr.employee', string='Employee')

    country = fields.Many2one('res.country', string="Country", tracking=True)
    degree_id = fields.Many2one('employee.degree', string="Degree")
    university_id = fields.Many2one('employee.university', string="University")
    faculty_id = fields.Many2one('employee.faculty', string="Faculty")
    major = fields.Char(string='Major')
    education_start_date = fields.Date(string='Start Date')
    education_end_date = fields.Date(string='End Date')
    batch_no = fields.Integer(string='Batch No')
    education_remarks = fields.Char(string='Remarks')



class EmployeeUniversity(models.Model):
    _name = 'employee.university'
    _description = 'Employee University'

    name = fields.Char(string='University')

class EmployeeDegree(models.Model):
    _name = 'employee.degree'
    _description = 'Employee Degree'

    name = fields.Char(string='Degree')


class EmployeeFaculty(models.Model):
    _name = 'employee.faculty'
    _description = 'Employee Faculty'

    name = fields.Char(string='faculty')





