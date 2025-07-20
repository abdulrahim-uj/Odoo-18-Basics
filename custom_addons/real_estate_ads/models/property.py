from email.policy import default

from odoo import fields, models


class Property(models.Model):
    _name = "estate.property"   # estate_property
    _description = "Real Estate Property"

    SELECTION_CHOICES = [
        ('north', "North"),
        ('south', "South"),
        ('east', "East"),
        ('west', "West")
    ]

    name = fields.Char(string="Name", required=True)
    tag_ids = fields.Many2many('estate.property.tag', string="Property Tag")
    type_id = fields.Many2one('estate.property.type', string="Property Type")
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Post Code")
    date_availability = fields.Date(string="Available From")
    expected_price = fields.Float(string="Expected Price")
    best_offer = fields.Float(string="Best Offer Price")
    selling_price = fields.Float(string="Selling Price")
    bedrooms = fields.Integer(string="Bedrooms")
    living_area = fields.Integer(string="Living Area(Sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage", default=False)
    garden = fields.Boolean(string="Garden", default=False)
    garden_area = fields.Integer(string="Garden Area(Sqm)")
    garden_orientation = fields.Selection(selection=SELECTION_CHOICES, string="Garden Orientation", default="north")
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string="Offers")
    sales_id = fields.Many2one('res.users', string="Salesman")
    buyer_id = fields.Many2one('res.partner', string="Buyer")
    # id, create_date, create_uid, write_date, write_uid   : odoo default creations


class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Property type description"

    name = fields.Char(string="Name", required=True)


class PropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Property tags description"

    name = fields.Char(string="Name", required=True)
