from .models import Event

def create_event(title, description, start_time, end_time):
    event = Event.objects.create(title=title, description=description, start_time=start_time, end_time=end_time)
    return event

def update_event(event_id, title=None, description=None, start_time=None, end_time=None):
    event = Event.objects.get(id=event_id)
    if title:
        event.title = title
    if description:
        event.description = description
    if start_time:
        event.start_time = start_time
    if end_time:
        event.end_time = end_time
    event.save()
    return event