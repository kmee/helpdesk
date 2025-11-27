import odoo.http as http
from odoo.http import request

from odoo.addons.helpdesk_mgmt.controllers.main import HelpdeskTicketController


class HelpdeskTicketController(HelpdeskTicketController):
    @http.route("/submitted/ticket", type="http", auth="user", website=True, csrf=True)
    def submit_ticket(self, **kw):
        res = super(HelpdeskTicketController, self).submit_ticket(**kw)
        ticket_id = res.location.split("/")[-1]
        new_ticket = request.env["helpdesk.ticket"].browse(int(ticket_id))
        if kw.get("followers"):
            emails = [
                email.strip()
                for email in kw.get("followers").split(",")
                if email.strip()
            ]
            partner_ids = []
            for email in emails:
                partners = request.env["res.partner"].search([("email", "=", email)])
                if not partners:
                    partner = (
                        request.env["res.partner"]
                        .sudo()
                        .create({"name": email, "email": email, "type": "contact"})
                    )
                    partner_ids.append(partner.id)
                else:
                    partner_ids.extend(partners.ids)
            new_ticket.sudo().message_subscribe(partner_ids=partner_ids)
        return res
