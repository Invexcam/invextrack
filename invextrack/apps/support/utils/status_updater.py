from ..models.ticket import Ticket

def update_ticket_status(ticket_id, status):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.status = status
    ticket.save()
    return ticket