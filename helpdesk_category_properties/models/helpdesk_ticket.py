from odoo import fields, models


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    ticket_properties = fields.Properties(
        "Properties", definition="category_id.ticket_properties_definition", copy=True
    )
