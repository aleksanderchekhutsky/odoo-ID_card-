from odoo import  fields, models, api
from odoo.exceptions import UserError, RedirectWarning, ValidationError
class PassportId(models.Model):


    _name ='passport.id'
    _description = 'Passport'


    name =fields.Char(string="Name")
    lastname = fields.Char(string="Lastname")
    cit = fields.Char(string="CIT")
    personalnum = fields.Float(string="Personal N", size=13,digits=(13,0))
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], required=True, default='male')
    birthdata = fields.Date(string="Date of birth")
    placebirth = fields.Char(strin="Place of birth")
    dateiss= fields.Date(string="Date of issue")
    image =fields.Binary(string="Image")
    other = fields.Many2one("passport.many", "deppartment")
    hobbies = fields.Many2many("hobie.many", string="hobie")

    #personal number validator
    @api.constrains('personalnum')
    def check_pers_num(self):
        if len(str(self.personalnum)) != 13:
            raise ValidationError(('personal  number length is not 11 '))
        else:
            for rec in self:
                nums = self.env['passport.id'].search([('personalnum','=',rec.personalnum),('id','!=',rec.id)])
                if nums:
                    raise ValidationError(("Personal number is used"))

    @api.constrains('birthdata')

    def check_name(self):
        for i in self:
            if i.birthdata ==0:
                raise ValidationError(("Enter age"))
    @api.constrains('name', 'lastname')
    def check_nam_lastnam(self):
        if self.name == False or self.lastname ==False:
            raise ValidationError(("Name or Lastname Error"))
    

class HobieMany(models.Model):
    _name = "hobie.many"
    _description = "hobie many"
    _rec_name = "hobi_list"
    hobi_list = fields.Char('Hobbie')

class PassportMany(models.Model):
    _name = "passport.many"
    _description = "passport many"
    _rec_name = 'other_list'


    other_list = fields.Char('other')





