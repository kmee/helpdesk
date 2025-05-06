from odoo import fields, models


class HelpdeskCategory(models.Model):
    _inherit = "helpdesk.ticket.category"

    substate_type_id = fields.Many2one(
        "base.substate.type",
        string="Substate Type",
        domain=[("model", "=", "helpdesk.ticket")],
        help="Define the substate type for tickets in this category",
    )
