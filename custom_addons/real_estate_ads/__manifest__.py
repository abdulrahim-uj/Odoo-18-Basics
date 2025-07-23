{
    "name": "Real Estate Advertisment",
    "version": "1.0.0",
    "website": "https://www.odoo.com/",
    "author": "AbdulRahim K",
    "description": """
        This is this module description.
    """,
    "category": "Sales",
    "depends": ['base'],
    "data": [
        # VIEW FILES
        "security/ir.model.access.csv",
        "views/property_view.xml",
        "views/property_type_view.xml",
        "views/property_tag_view.xml",
        "views/menu_items.xml",
        # DATA FILES
        # "data/property_type.xml",
        "data/estate.property.type.csv",
    ],
    "demo": [
        # "demo/property_tag.xml",
        "demo/estate.property.tag.csv",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3"
}
