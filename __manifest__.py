{
    "name": "EGP HR Employee",
    "version": "17.0.1.0.0",
    "summary": "EGP Human Resource Module",
    'sequence': -100,
    'category': 'Human Resources',
    "description": "",
    'depends': ['hr', 'mail', 'hr_recruitment', 'hr_skills', 'egp_hr_org_structure', 'egp_hr_recruitment'],
    'data': [
        'security/egp_hr_security/egp_hr_employee_security.xml',
        'security/egp_hr_security/ir.model.access.csv',
        'views/egp_hr_employee_views/egp_hr_employee.xml',
        'views/egp_hr_employee_views/egp_hr_applicant.xml',
        'data/egp_hr_employee_default_data/egp_hr_employee_default_data.xml',
        # 'data/egp_hr_employee_default_data/res.country.state.csv',
        # 'data/egp_hr_employee_default_data/res.country.data.xml',
        'report/egp_hr_employee_report.xml',
        # 'report/egp_hr_report_paper_format.xml',
        'views/egp_hr_employee_views/egp_hr_print_action.xml',

    ],
    "author": "Nasratullah Shafiq",
    "website": "https://mcit.gov.af/",
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": 'OPL-1',
}

