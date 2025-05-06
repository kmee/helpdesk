{
    "name": "Helpdesk Category Substates",
    "summary": "Add substates to helpdesk tickets based on their category",
    "version": "16.0.1.0.0",
    "category": "Helpdesk",
    "website": "https://github.com/OCA/helpdesk",
    "author": "",
    "license": "AGPL-3",
    "depends": ["helpdesk_mgmt", "base_substate"],
    "data": [
        "views/helpdesk_ticket_category_views.xml",
        "views/helpdesk_ticket_views.xml",
        "security/ir.model.access.csv",
        "data/helpdesk_substate_data.xml",
    ],
    "demo": [
        "demo/helpdesk_substate_demo.xml",
    ],
    "application": False,
    "installable": True,
}
