from odoo import http
from odoo.http import request

class JobApplication(http.Controller):

    @http.route('/apply_form/', auth='public', website=True)
    def render_job_personal_form(self, **kw):
        applicants = request.env['hr.applicant'].sudo().search([])
        return request.render('egp_hr.personal_information_form_template', {'applicants': applicants})

class ApplicantController(http.Controller):

    @http.route('/submit_applicant', type='http', auth="public", website=True, methods=['POST'])
    def submit_applicant(self, **post):
        # Retrieve form data
        name = post.get('name')
        email = post.get('email')
        phone = post.get('phone')
        resume = request.httprequest.files.get('resume')

        # Create hr.applicant record
        applicant = request.env['hr.applicant'].sudo().create({
            'name': name,
            'email_from': email,
            'phone': phone,
            # Additional fields can be added here as needed
        })

        # Handle resume attachment
        if resume:
            attachment = request.env['ir.attachment'].sudo().create({
                'name': resume.filename,
                'type': 'binary',
                'datas': resume.read(),
                'res_model': 'hr.applicant',
                'res_id': applicant.id,
            })
            applicant.write({'attachment_ids': [(4, attachment.id)]})

        # Redirect or display success message
        return request.render('egp_hr.success_message_form_template')

