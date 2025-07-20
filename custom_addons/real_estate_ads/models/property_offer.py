from odoo import fields, models


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
