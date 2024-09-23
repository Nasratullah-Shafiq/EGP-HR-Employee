# -*- coding: utf-8 -*-
from odoo import fields, models, api


class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'
    _description = "Human Resource"

    fire_ids = fields.One2many('employee.fire', 'employee_id', string='Fire')


# Your Python code (e.g., in a controller or model)

class EmployeeFire(models.Model):
    _name = 'employee.fire'
    _description = 'Employee Fire'

    employee_id = fields.Many2one('hr.employee', string='Employee')

    fire_type = fields.Many2one('employee.fire.type', string='Fire Type', Tracking='true')
    leave_reason = fields.Many2one('employee.leave.reason', string='reason for leaving the job', Tracking='true')

    order_date = fields.Date(string='Order Date', Tracking='true')
    order_no = fields.Integer(string='Order No', Tracking='true')
    date_approved = fields.Date(string='Date Approved', Tracking='true')
    fire_remarks = fields.Char(string='Remarks', Tracking='true')

    class EmployeeLeaveReason(models.Model):
        _name = 'employee.leave.reason'
        _description = 'Employee Document Type'
        name = fields.Char(string='Document Type')

    class EmployeeFireType(models.Model):
        _name = 'employee.fire.type'
        _description = 'Employee Fire Type'

        name = fields.Char(string='Document Type')

