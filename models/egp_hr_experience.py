# -*- coding: utf-8 -*-
from odoo import fields, models, api


class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'
    _description = "Human Resource"

    experience_ids = fields.One2many('employee.experience', 'employee_id', string='Experience')


# Your Python code (e.g., in a controller or model)

class EmployeeExperience(models.Model):
    _name = 'employee.experience'
    _description = 'Employee Experience'

    employee_id = fields.Many2one('hr.employee', string='Employee')

    country = fields.Many2one('res.country', string="Country", tracking=True, ondelete='cascade')
    province = fields.Many2one('res.country.state', string="Province", tracking=True, ondelete='cascade')
    organization_id = fields.Many2one('employee.organization', string="Organization")
    job_position = fields.Char(string='Job Position')
    grade = fields.Selection([('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th'),
                              ('6th', '6th'), ('7th', '7th'), ('8th', '8th')], string="Grade")
    step_id = fields.Many2one('employee.step', string="Step or Rank")
    department = fields.Char(string='Department')
    status_id = fields.Many2one('employee.status', string="Status")
    job_start_date = fields.Date(string='Start Date')
    job_end_date = fields.Date(string='End Date')
    organization_type = fields.Selection([('Civil', 'Civil'), ('Military', 'Military'), ('NGO', 'NGO'),
                                          ('international_organization', 'International Organization'),
                                          ('united_nations', 'United Nations')], string="Organization Type")
    job_remarks = fields.Char(string='Remarks')
    duration_days = fields.Integer('Duration Days (Days)', compute='_compute_duration_days', store=True)

    @api.depends('job_start_date', 'job_end_date')
    def _compute_duration_days(self):
        for record in self:
            if record.job_start_date and record.job_end_date:
                delta = record.job_end_date - record.job_start_date
                record.duration_days = delta.days
                # record.duration_years = delta.days
                # record.duration_months = delta.months
            else:
                record.duration_days = 0
                # record.duration_months = 0

class EmployeeOrganization(models.Model):
    _name = 'employee.organization'
    _description = 'Employee Organization'

    name = fields.Char(string='Organization')


class EmployeeStep(models.Model):
    _name = 'employee.step'
    _description = 'Employee Step'

    name = fields.Char(string='Step Or Rank')

class EmployeeStatus(models.Model):
    _name = 'employee.status'
    _description = 'Employee Status'

    name = fields.Char(string='Status')






















