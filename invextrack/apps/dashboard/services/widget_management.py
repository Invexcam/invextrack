from ..models.widget import Widget

def create_widget(title, description, config):
    widget = Widget.objects.create(title=title, description=description, config=config)
    return widget

def update_widget(widget_id, title=None, description=None, config=None):
    widget = Widget.objects.get(id=widget_id)
    if title:
        widget.title = title
    if description:
        widget.description = description
    if config:
        widget.config = config
    widget.save()
    return widget