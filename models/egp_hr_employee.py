# -*- coding: utf-8 -*-
from odoo import fields, models, api


class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'
    _description = "Human Resource"

    father_name = fields.Char(string='Father Name')
    grand_father_name = fields.Char(string='Grand Father Name')

    job_step = fields.Selection([('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th')],
                                string='Step')
    message_main_attachment_id = fields.Many2one(groups="base.group_erp_manager,egp_hr.group_employee_officers,egp_hr.group_employee_expert")

    recruitment_date = fields.Date(string='Recruitment Date')

    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')

    identification_type = fields.Selection([('paper_id_card', 'Paper ID card'),
                                            ('electronic_id_card', 'Electronic ID Card')],
                                string='ID Card')
    identification_no = fields.Char(string='Identification No')
    identification_print_date = fields.Date(string='Print Date')
    identification_expiry_date = fields.Date(string='Expire Date')
    identification_chapter = fields.Integer(string='Chapter')
    identification_page_no = fields.Integer(string='Page No')
    # permanent_province = fields.Many2one('res.country.state', string="Permanent Province", tracking=True, ondelete='cascade')
    # temporary_province = fields.Many2one('res.country.state', string="Temporary Province", tracking=True, ondelete='cascade')
    # Use the same variable for both fields

    permanent_district = fields.Many2one('employee.district', string="Permanent District", tracking=True,
                                         ondelete='cascade')
    temporary_district = fields.Many2one('employee.district', string="Temporary District", tracking=True,
                                         ondelete='cascade')
    permanent_village = fields.Char(string='Permanent Village')
    temporary_village = fields.Char(string='Temporary Village')
    home_number = fields.Integer(string='Home Number')
    permanent_street = fields.Char(string='Permanent Street')
    private_streets = fields.Char(string='Private Street')
    passport_print_date = fields.Date(string='Print Date')
    passport_end_date = fields.Date(string='Expiry Date')

    emp_gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender')
    emp_date_of_birth = fields.Date(string='Date Of Birth')
    emp_place_of_birth = fields.Many2one('res.country.state', string="Place of Birth", tracking=True,
                                         ondelete='cascade')
    emp_country_of_birth = fields.Many2one('res.country', string="Country of Birth", tracking=True,ondelete='cascade')
    emp_nationality = fields.Many2one('res.country', string="Nationality", tracking=True,ondelete='cascade')
    # Define the list of provinces once
    PROVINCES = [
        ('Badakhshan', 'Badakhshan'),
        ('Badghis', 'Badghis'),
        ('Baghlan', 'Baghlan'),
        ('Balkh', 'Balkh'),
        ('Bamyan', 'Bamyan'),
        ('Daykundi', 'Daykundi'),
        ('Farah', 'Farah'),
        ('Faryab', 'Faryab'),
        ('Ghazni', 'Ghazni'),
        ('Ghor', 'Ghor'),
        ('Helmand', 'Helmand'),
        ('Herat', 'Herat'),
        ('Jowzjan', 'Jowzjan'),
        ('Kabul', 'Kabul'),
        ('Kandahar', 'Kandahar'),
        ('Kapisa', 'Kapisa'),
        ('Khost', 'Khost'),
        ('Kunar', 'Kunar'),
        ('Kunduz', 'Kunduz'),
        ('Laghman', 'Laghman'),
        ('Logar', 'Logar'),
        ('Nangarhar', 'Nangarhar'),
        ('Nimroz', 'Nimroz'),
        ('Nuristan', 'Nuristan'),
        ('Paktia', 'Paktia'),
        ('Paktika', 'Paktika'),
        ('Panjshir', 'Panjshir'),
        ('Parwan', 'Parwan'),
        ('Samangan', 'Samangan'),
        ('Sar-e Pol', 'Sar-e Pol'),
        ('Takhar', 'Takhar'),
        ('Urozgan', 'Urozgan'),
        ('Wardak', 'Wardak'),
        ('Zabul', 'Zabul')
    ]
    permanent_province = fields.Selection(PROVINCES, string="Province")
    temporary_province = fields.Selection(PROVINCES, string="Province")


