from reportlab.graphics.transform import inverse
from datetime import timedelta
from odoo import fields, models, api


class PropertyOffer(models.Model):
    """ This model represents property.offer."""
    _name = 'estate.property.offer'
    _description = 'Estate Property Offer'

    SELECTION_CHOICES = [
        ('accepted', "Accepted"),
        ('refused', "Refused")
    ]

    price = fields.Float(string="Price")
    status = fields.Selection(selection=SELECTION_CHOICES, string="Staus", )
    partner_id = fields.Many2one('res.partner', string="Customer")
    property_id = fields.Many2one('estate.property', string="Property")
    validity = fields.Integer(string="Validity")
    deadline = fields.Date(string='Deadline', compute='_compute_deadline', inverse='_inverse_deadline', store=True)
    creation_date = fields.Date(string="Creation Date")

    @api.depends('validity', 'creation_date')
    def _compute_deadline(self):
        """Compute the value of the field deadline."""
        for record in self:
            if record.creation_date and record.validity:
                record.deadline = record.creation_date + timedelta(days=record.validity)  # Your computation here
            else:
                record.deadline = False

    def _inverse_deadline(self):
        for record in self:
            record.validity = (record.deadline - record.creation_date).days
