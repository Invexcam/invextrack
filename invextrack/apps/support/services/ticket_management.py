from ..models.ticket import Ticket

def create_ticket(title, description, category):
    ticket = Ticket.objects.create(title=title, description=description, category=category)
    return ticket

def update_ticket(ticket_id, title=None, description=None, category=None):
    ticket = Ticket.objects.get(id=ticket_id)
    if title:
        ticket.title = title
    if description:
        ticket.description = description
    if category:
        ticket.category = category
    ticket.save()
    return ticket