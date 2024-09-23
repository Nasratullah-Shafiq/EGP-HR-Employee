# -*- coding: utf-8 -*-
from odoo import fields, models, api

class EmployeeDistrict(models.Model):
    _name = 'employee.district'
    _description = 'Employee District'

    name = fields.Char(string='District')


class EmployeeVillage(models.Model):
    _name = 'employee.village'
    _description = 'Employee Village'

    name = fields.Char(string='Village')




