from odoo import api, fields, models


class HelpdeskTicket(models.Model):
    _name = "helpdesk.ticket"
    _inherit = ["helpdesk.ticket", "base.substate.mixin"]

    def _get_substate_type(self):
        if self.category_id and self.category_id.substate_type_id:
            return self.category_id.substate_type_id
        return super()._get_substate_type()

    @api.onchange("category_id")
    def _onchange_category_id(self):
        if self.category_id and self.category_id.substate_type_id:
            self.substate_id = self._get_default_substate_id()
