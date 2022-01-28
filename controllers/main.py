from odoo import http
from odoo.http import request
import json
import openerp


class Passport(http.Controller):

    @http.route('/passport/json/', type='json', auth='public',csrf=False,methods=['GET'])
    def json(self, **post):
        """Returns users data from json"""

        passport_rec = request.env['passport.id'].search([])
        ids = []
        for i in passport_rec:
            vals = {
                'name': i.name,
                'lastname': i.last_name,
                'CIT': i.cit,
                'personal_n': i.personal_num,
                'gender': i.gender,
                'date_of_birth': i.birth_of_data,
                'place_of_birth': i.place_of_birth,
                'date_of_issue' : i.date_of_iss,
                'department':i.other.other_list,
                'hobbies': i.hobbies
            }
            ids.append(vals)
        data = {'status': 200, 'response': ids, 'message': 'Success'}
        return data

