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
    other = fields.Many2one("passport.many", string="Department", reqired=True)
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
            if not str(i.personal_num).isdigit():
                raise ValidationError('Personal number is not corect!')

    @api.constrains('name', 'last_name')
    def check_nam_lastnam(self):
        """Name and Lastname validation"""
        for i in self:
            if i.name == i.last_name:
                raise ValidationError(("Name or Lastname Error"))
            if not i.name.isalpha():
                raise ValidationError(("Name Error!"))
            if not i.last_name.isalpha():
                raise ValidationError(("Lastname Error!"))
            else:
                if i.name[0].islower():
                    i.name = i.name.capitalize()
                if i.last_name[0].islower():
                    i.last_name = i.last_name.capitalize()


    @api.constrains('cit','place_of_birth')
    def check_cit_and_place(self):
        """ Cit and Place Of birth validation"""
        for i in self:
            if not i.cit.isalpha():
                raise ValidationError("CIT or Place Error! ")
            if not i.place_of_birth.isalpha():
                raise ValidationError("Place of birth Error!")
            else:
                if i.cit.islower():
                    i.cit = i.cit.upper()
                if i.place_of_birth[0].islower():
                    i.place_of_birth = i.place_of_birth.capitalize()


class PassportHobie(models.Model):
    _name = "passport.hobie"
    _description = "passport hobie"
    _rec_name = "passport_hobi"

    passport_hobi = fields.Char('Hobbie')


class PassportMany(models.Model):
    _name = "passport.many"
    _description = "passport many"
    _rec_name = 'passport_other'

    passport_other = fields.Char(string='Department', size=20, required =True)
    passport_employe =fields.One2many('passport.id', 'other', string='Employee')
    passport_manager = fields.Many2one('passport.id', string='Manager')

