# -*- coding: utf-8 -*-
from odoo import fields, models, api


class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'
    _description = "Human Resource"

    attachment_ids = fields.One2many('employee.document', 'employee_id', string='Document')


# Your Python code (e.g., in a controller or model)

class EmployeeAttachment(models.Model):
    _name = 'employee.document'
    _description = 'Employee Document'

    employee_id = fields.Many2one('hr.employee', string='Employee')
    document_type = fields.Many2one('employee.document.type', string='Document Type', Tracking='true')

    document_remarks = fields.Char(string='Remarks', Tracking='true')
    document_name = fields.Char(string='Document Name', Tracking='true')
    status = fields.Selection([('active', 'Active'), ('archive', 'Archive')], string="Status", default='active', Tracking='true')

class EmployeeDocumentType(models.Model):
    _name = 'employee.document.type'
    _description = 'Employee Document Type'

    name = fields.Char(string='Document Type')
