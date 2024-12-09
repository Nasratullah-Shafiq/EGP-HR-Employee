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

    province = fields.Selection([
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
    ], string="Province")

    organization_id = fields.Many2one('employee.organization', string="Organization")
    job_position = fields.Char(string='Job Position')
    # grade = fields.Selection([('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th'),
    #                           ('6th', '6th'), ('7th', '7th'), ('8th', '8th')], string="Grade")

    grade = fields.Selection([
        ('major_general', 'Major General'),
        ('lieutenant_general', 'Lieutenant Genenral'),
        ('accused_general', 'Accused General'),
        ('brigadier_general', 'Brigadier General'),
        ('colonel', 'Colonel'),
        ('lieutenant', 'Lieutenant'),
        ('battler', 'Battler'),
        ('accused', 'Accused'),
        ('first_lieutenant', 'First Lieutenant'),
        ('second_lieutenant', 'Second Lieutenant'),
        ('acting_sergeant', 'Acting Sergeant'),
        ('assistant_acting_sergeant', 'Assistant Acting Sergeant'),
        ('chief_sergeant', 'Chief Sergeant'),
        ('superior_rank', 'Superior Rank'),
        ('grade_one', 'Grade 1'),
        ('grade_two', 'Grade 2'),
        ('grade_three', 'Grade 3'),
        ('grade_four', 'Grade 4'),
        ('grade_five', 'Grade 5'),
        ('grade_six', 'Grade 6'),
        ('grade_seven', 'Grade 7'),
        ('grade_eight', 'Grade 8'),
        ('grade_nine', 'Grade 9'),
        ('grade_ten', 'Grade 10'),
        ('outside_rank', 'Outside Rank'),
        ('above_rank', 'Above Rank'),
        ('assistant_chief', 'Assistant Chief'),
        ('chief', 'Chief'),
        ('jungle_chief', 'Jungle Chief'),
        ('chief_of_regiment', 'Chief of Regiment'),
        ('without_rank', 'Without Rank'),
        ('soldier_or_officer', 'Soldier / Officer'),
        ('judicial_branch_one', 'Judicial Branch 1'),
        ('judicial_branch_two', 'Judicial Branch 2'),
        ('judicial_branch_three', 'Judicial Branch 3'),
        ('judicial_branch_four', 'Judicial Branch 4'),
        ('judicial_partner', 'Judicial Partner'),
        ('judicial_level', 'Judicial Level'),
        ('above_degree', 'Above Degree'),
        ('first_position', 'First Position'),
        ('second_position', 'Second Position'),
        ('third_position', 'Third Position'),
        ('fourth_position', 'Fourth Position'),
        ('fourth_position', 'Fourth Position'),
        ('fifth_position', 'Fifth Position'),
        ('sixth_position', 'Sixth Position'),
        ('seventh_position', 'Seventh Position'),
        ('eight_position', 'Eight Position'),
        ('ninth_position', 'Ninth Position'),
        ('tenth_position', 'Tenth Position')
    ], string="Grade")





    step = fields.Selection([
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
    ], string="Step / Rank")
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


class EmployeeStatus(models.Model):
    _name = 'employee.status'
    _description = 'Employee Status'

    name = fields.Char(string='Status')






















