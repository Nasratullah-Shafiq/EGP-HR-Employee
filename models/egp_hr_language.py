from odoo import api, fields, models

class EgpHrInherit(models.Model):
    _inherit = 'hr.employee'
    _description = "Human Resource"

    language_ids = fields.One2many('employee.language', 'employee_id', string='Language')


# Your Python code (e.g., in a controller or model)

class EmployeeLanguage(models.Model):
    _name = 'employee.language'
    _description = 'Language'

    employee_id = fields.Many2one('hr.employee', string='Employee')
    language = fields.Char(string='Language')
    reading = fields.Selection([('good', 'Good'), ('َvery_good', 'Very Good'),
                                ('excellent', 'Excellent'), ], string="Reading", default='excellent')
    speaking = fields.Selection([('good', 'Good'), ('َvery_good', 'Very Good'),
                                 ('excellent', 'Excellent'), ], string="Speaking", default='excellent')
    listening = fields.Selection([('good', 'Good'), ('َvery_good', 'Very Good'),
                                  ('excellent', 'Excellent'), ], string="Listening", default='excellent')
    writing = fields.Selection([('good', 'Good'), ('َvery_good', 'Very Good'),
                                ('excellent', 'Excellent'), ], string="Writing", default='excellent')
