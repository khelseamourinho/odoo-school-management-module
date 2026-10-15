# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class SchoolAbsensi(models.Model):
    _name = "school.absensi"
    _description = "For Input Students Absensi"
    
    absensi_date = fields.Date(string='Absensi')
    student_ids = fields.Many2many('school.student', string='Students')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('progress', 'On Progress'),
        ('done', 'Done'),
    ], string='State', default='draft', required=True)
