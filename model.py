# -- coding: utf-8 -- 

from odoo import models, fields


class ProfesorRecord(models.Model):

    _name = "academia.profesor"
    _inherits = {'res.partner': 'partner_id'}
    partner_id = fields.Many2one('res.partner',ondelete='cascade',require=True)

class AsignaturaRecord(models.Model):

    _name = "academia.asignatura"
    nombre = fields.Char(string='Nombre', required=True)
    temas = fields.Integer(string='Temas')
    tipo = fields.Selection([('c', 'Ciencias'), ('l', 'Letras'), ('i', 'Idiomas'), ('o', 'Otro')], string='Tipo')
    profesor = fields.Many2one('academia.profesor', string='Profesor')

    