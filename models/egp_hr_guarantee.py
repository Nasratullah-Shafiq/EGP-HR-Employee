# -*- coding: utf-8 -*-
from odoo import fields, models, api


class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'
    _description = "Human Resource"

    cash_guarantee_ids = fields.One2many('employee.cash.guarantee', 'employee_id', string='Guarantee')
    person_guarantee_ids = fields.One2many('employee.person.guarantee', 'employee_id', string='Guarantee')
    property_guarantee_ids = fields.One2many('employee.property.guarantee', 'employee_id', string='Guarantee')


# Your Python code (e.g., in a controller or model)

class CashGuarantee(models.Model):
    _name = 'employee.cash.guarantee'
    _description = 'Employee Cash Guarantee'

    employee_id = fields.Many2one('hr.employee', string='Employee')

    amount_of_cash = fields.Integer(string='Amount of Cash')
    bank_name = fields.Char(string='Bank Name')
    bank_slip_no = fields.Integer(string='Bank Slip No')
    cash_remarks = fields.Char(string='Remarks')


    class PropertyGuarantee(models.Model):
        _name = 'employee.property.guarantee'
        _description = 'Employee Property Guarantee'

        employee_id = fields.Many2one('hr.employee', string='Employee')

        # location = fields.Char(string='Location')
        property_province_id = fields.Many2one('res.country.state', string="Province", tracking=True,
                                                ondelete='cascade')
        property_district_id = fields.Many2one('employee.district', string="District")
        property_village_id = fields.Many2one('employee.village', string="Village")
        deed_no = fields.Integer(string='Deed No')
        deed_date = fields.Date(string='Deed Date')
        property_remarks = fields.Char(string='Remarks')


class PersonGuarantee(models.Model):
    _name = 'employee.person.guarantee'
    _description = 'Employee Person Guarantee'

    employee_id = fields.Many2one('hr.employee', string='Employee')

    person_name = fields.Char(string='Name')
    last_name = fields.Char(string='Last Name')
    father_name = fields.Char(string='Father Name')
    grand_father_name = fields.Char(string='Grand Father Name')
    job_position = fields.Char(string='Job Position')
    organization = fields.Char(string='Organization')
    permanent_province_id = fields.Many2one('res.country.state', string="Province", tracking=True, ondelete='cascade')
    permanent_district_id = fields.Many2one('employee.district', string="District")
    permanent_village_id = fields.Many2one('employee.village', string="Village")

    temporary_province_id = fields.Many2one('res.country.state', string="Province", tracking=True, ondelete='cascade')
    temporary_district_id = fields.Many2one('employee.district', string="District")
    temporary_village_id = fields.Many2one('employee.village', string="Village")
    phone_no = fields.Char(string='Phone No')
    email = fields.Char(string='Email')