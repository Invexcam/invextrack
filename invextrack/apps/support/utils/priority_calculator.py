def calculate_priority(ticket):
    # Example priority calculation logic
    priority = 1
    if 'urgent' in ticket.description.lower():
        priority = 5
    return priority