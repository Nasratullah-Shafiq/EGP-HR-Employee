# -*- coding: utf-8 -*-
from odoo import fields, models, api


class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'
    _description = "Human Resource"

    father_name = fields.Char(string='Father Name', groups="egp_hr.group_employee_officers,egp_hr.group_employee_expert")
    grand_father_name = fields.Char(string='Grand Father Name', groups="egp_hr.group_employee_officers,egp_hr.group_employee_expert")

    job_step = fields.Selection([
        ('first_step', 'First Step'),
        ('second_step', 'Second Step'),
        ('third_step', 'Third Step'),
        ('fourth_step', 'Fourth Step'),
        ('fourth_step', 'Fourth Step'),
        ('fifth_step', 'Fifth Step'),
        ('sixth_step', 'Sixth Step'),
        ('seventh_step', 'Seventh Step'),
        ('eight_step', 'Eight Step'),
        ('ninth_step', 'Ninth Step'),
        ('tenth_step', 'Tenth Step'),
        ('first_rank', 'First Rank'),
        ('second_rank', 'Second Rank'),
        ('third_rank', 'Third Rank'),
        ('fourth_rank', 'Fourth Rank'),
        ('fourth_rank', 'Fourth Rank'),
        ('fifth_rank', 'Fifth Rank'),
        ('sixth_rank', 'Sixth Rank'),
        ('seventh_rank', 'Seventh Rank'),
        ('eight_rank', 'Eight Rank'),
        ('ninth_rank', 'Ninth Rank'),
        ('tenth_rank', 'Tenth Rank'),
        ('super_rank', 'Super Rank'),
        ('superior_rank', 'Superior Rank'),
        ('unranked', 'Unranked'),
        ('prof', 'Professor'),
        ('scholar', 'Scholar'),
        ('phanmal', 'Pohanmal'),
        ('pohand', 'Pohand')
    ], string="Step / Rank", groups="egp_hr.group_employee_officers,egp_hr.group_employee_expert")


    message_main_attachment_id = fields.Many2one(groups="base.group_erp_manager,egp_hr.group_employee_officers,egp_hr.group_employee_expert")

    recruitment_date = fields.Date(string='Recruitment Date', groups="egp_hr.group_employee_officers,egp_hr.group_employee_expert")

    start_date = fields.Date(string='Start Date', groups="egp_hr.group_employee_officers,egp_hr.group_employee_expert")
    end_date = fields.Date(string='End Date', groups="egp_hr.group_employee_officers,egp_hr.group_employee_expert")

    identification_type = fields.Selection([('paper_id_card', 'Paper ID card'),
                                            ('electronic_id_card', 'Electronic ID Card')],
                                string='ID Card', groups="egp_hr.group_employee_officers,egp_hr.group_employee_expert")
    identification_no = fields.Char(string='Identification No', groups="egp_hr.group_employee_officers,egp_hr.group_employee_expert")
    identification_print_date = fields.Date(string='Print Date', groups="egp_hr.group_employee_officers,egp_hr.group_employee_expert")
    identification_expiry_date = fields.Date(string='Expire Date', groups="egp_hr.group_employee_officers,egp_hr.group_employee_expert")
    identification_chapter = fields.Integer(string='Chapter', groups="egp_hr.group_employee_officers,egp_hr.group_employee_expert")
    identification_page_no = fields.Integer(string='Page No', groups="egp_hr.group_employee_officers,egp_hr.group_employee_expert")
    # permanent_province = fields.Many2one('res.country.state', string="Permanent Province", tracking=True, ondelete='cascade')
    # temporary_province = fields.Many2one('res.country.state', string="Temporary Province", tracking=True, ondelete='cascade')
    # Use the same variable for both fields

    permanent_district = fields.Many2one('employee.district', string="Permanent District", tracking=True,
                                         ondelete='cascade', groups="egp_hr.group_employee_officers,egp_hr.group_employee_expert")
    temporary_district = fields.Many2one('employee.district', string="Temporary District", tracking=True,
                                         ondelete='cascade', groups="egp_hr.group_employee_officers,egp_hr.group_employee_expert")
    permanent_village = fields.Char(string='Permanent Village', groups="egp_hr.group_employee_officers,egp_hr.group_employee_expert")
    temporary_village = fields.Char(string='Temporary Village', groups="egp_hr.group_employee_officers,egp_hr.group_employee_expert")
    home_number = fields.Integer(string='Home Number', groups="egp_hr.group_employee_officers,egp_hr.group_employee_expert")
    permanent_street = fields.Char(string='Permanent Street', groups="egp_hr.group_employee_officers,egp_hr.group_employee_expert")
    private_streets = fields.Char(string='Private Street', groups="egp_hr.group_employee_officers,egp_hr.group_employee_expert")
    passport_print_date = fields.Date(string='Print Date', groups="egp_hr.group_employee_officers,egp_hr.group_employee_expert")
    passport_end_date = fields.Date(string='Expiry Date', groups="egp_hr.group_employee_officers,egp_hr.group_employee_expert")

    emp_gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender', groups="egp_hr.group_employee_officers,egp_hr.group_employee_expert")
    emp_date_of_birth = fields.Date(string='Date Of Birth', groups="egp_hr.group_employee_officers,egp_hr.group_employee_expert")
    emp_place_of_birth = fields.Many2one('res.country.state', string="Place of Birth", tracking=True,
                                         ondelete='cascade', groups="egp_hr.group_employee_officers,egp_hr.group_employee_expert")
    emp_country_of_birth = fields.Many2one('res.country', string="Country of Birth", tracking=True,ondelete='cascade', groups="egp_hr.group_employee_officers,egp_hr.group_employee_expert")
    emp_nationality = fields.Many2one('res.country', string="Nationality", tracking=True,ondelete='cascade', groups="egp_hr.group_employee_officers,egp_hr.group_employee_expert")
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
    permanent_province = fields.Selection(PROVINCES, string="Province", groups="egp_hr.group_employee_officers,egp_hr.group_employee_expert")
    temporary_province = fields.Selection(PROVINCES, string="Province", groups="egp_hr.group_employee_officers,egp_hr.group_employee_expert")


