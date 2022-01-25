from odoo import http
from odoo.http import request
import json
import openerp

class Passport(http.Controller):
    @http.route('/passport/json/', type='json', auth='public',csrf=False,methods=['GET'])
    def json(self, **post):
        passport_rec = request.env['passport.id'].search([])
        ids = []
        for i in passport_rec:
            vals = {

                'name': i.name,
                'lastname': i.lastname,
                'CIT': i.cit,
                'personal_n': i.personalnum,
                'gender': i.gender,
                'date_of_birth': i.birthdata,
                'place_of_birth': i.placebirth,
                'date_of_issue' : i.dateiss,
                'department':i.other.other_list,
                'hobbies': i.hobbies
                }
            ids.append(vals)
        data = {'status': 200, 'response': ids, 'message': 'Success'}
        return data

