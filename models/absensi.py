# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError 

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

    def write(self, vals):
        if self.state == 'done':
            raise UserError(_("You Cant Update Data After Done"))
        res = super(SchoolAbsensi, self).write(vals)
        return res