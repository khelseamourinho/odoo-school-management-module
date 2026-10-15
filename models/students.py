# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class SchoolStudents(models.Model):
    _name = "school.student"
    _description = "For Input Students Data"
    _order = "name"  # Standar Odoo Modern: Mengurutkan data list secara otomatis berdasarkan nama

    name = fields.Char(string='Students Name', required=True)
    student_class = fields.Selection([
        ('10', 'Grade 10'),
        ('11', 'Grade 11'),
        ('12', 'Grade 12'),
    ], string='Student Class', default='10',required=True)
    
    state = fields.Selection([
        ('undergraduate', 'Not Graduate'),
        ('graduated', 'Graduated'),
    ], string='State', required= True, default='undergraduate')

    def set_graduate(self):
        if self.state == 'undergraduate':
            self.state = 'graduated'
        return True