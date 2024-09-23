from odoo import api, fields, models

class EgpHrInherit(models.Model):
    _inherit = 'hr.employee'
    _description = "Human Resource"

    health_ids = fields.One2many('employee.health', 'employee_id', string='Health')


# Your Python code (e.g., in a controller or model)

class EmployeeHealth(models.Model):
    _name = 'employee.health'
    _description = 'Health'

    employee_id = fields.Many2one('hr.employee', string='Employee')
    health_status = fields.Selection([('good', 'Good'), ('َunder_treatment', 'Under Treatment'),
                                      ('under_operation', 'Under Operation'),], string="Status")
    health_report_date = fields.Date(string='Report Date')
    health_remarks = fields.Char(string='Remarks')
