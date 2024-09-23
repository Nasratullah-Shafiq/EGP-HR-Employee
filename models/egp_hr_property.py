# -*- coding: utf-8 -*-
from odoo import fields, models, api


class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'
    _description = "Human Resource"

    property_ids = fields.One2many('employee.property', 'employee_id', string='Property')

# Your Python code (e.g., in a controller or model)

class EmployeeProperty(models.Model):
    _name = 'employee.property'
    _description = 'Employee Property'

    employee_id = fields.Many2one('hr.employee', string='Employee')

    property_type = fields.Selection(
        [('movable_property', 'Movable Property'), ('nonmovable_peroperty', 'Non Movable Property'),
         ('car', 'Car'), ('land', 'Land'), ('home', 'Home'), ('market', 'Market'),
         ('garden', 'Garden'), ('cash', 'Cash'), ('jewelery', 'Jewelery'), ('house', 'House'),
         ('other', 'other')], string="Property")

    price = fields.Char(string='Price')
    remarks = fields.Char(string='Remarks')












