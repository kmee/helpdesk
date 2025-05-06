from odoo import fields, models


class BaseSubstateType(models.Model):
    _inherit = "base.substate.type"

    model = fields.Selection(
        selection_add=[("helpdesk.ticket", "Helpdesk Ticket")],
        ondelete={"helpdesk.ticket": "cascade"},
    )
