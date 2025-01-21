from ..models.task import Task

def create_task(name, description, due_date):
    task = Task.objects.create(name=name, description=description, due_date=due_date)
    return task

def update_task(task_id, name=None, description=None, due_date=None, completed=None):
    task = Task.objects.get(id=task_id)
    if name:
        task.name = name
    if description:
        task.description = description
    if due_date:
        task.due_date = due_date
    if completed is not None:
        task.completed = completed
    task.save()
    return task