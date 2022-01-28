from odoo import  fields, models, api
from odoo.exceptions import UserError, RedirectWarning, ValidationError


class PassportId(models.Model):
    _name = 'passport.id'
    _description = 'Passport'

    name = fields.Char(string="Name", required=True)
    last_name = fields.Char(string="Lastname", required=True)
    cit = fields.Char(string="CIT", required=True)
    personal_num = fields.Char(string="Personal N", size=11, digits=(11,0), required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], required=True, default='male')
    birth_of_data = fields.Date(string="Date of birth", required=True)
    place_of_birth = fields.Char(strin="Place of birth", required=True)
    date_of_iss = fields.Date(string="Date of issue", required=True)
    image = fields.Binary(string="Image")
    other = fields.Many2one("passport.many", "deppartment")
    hobbies = fields.Many2many("passport.hobie", string="hobie")

    _sql_constraints = [
        ('personal_number_unique',
         'unique(personal_num)',
         'Personal number already exists!')
    ]

    @api.constrains('personal_num')
    def personal_num_check(self):
        """Personal Number Validation"""
        for i in self:
            if len(i.personal_num) != 11:
                raise ValidationError('Personal  Number length is not 11 ')
            if str(i.personal_num).isdigit()!= True:
                raise ValidationError('Personal number is not corect!')

    @api.constrains('name', 'last_name')
    def check_nam_lastnam(self):
        """Name and Lastname validation"""
        for i in self:
            if self.name == self.last_name:
                raise ValidationError(("Name or Lastname Error"))


class PassportHobie(models.Model):
    _name = "passport.hobie"
    _description = "passport hobie"
    _rec_name = "hobi_list"

    hobi_list = fields.Char('Hobbie')


class PassportMany(models.Model):
    _name = "passport.many"
    _description = "passport many"
    _rec_name = 'other_list'

    other_list = fields.Char('other')
