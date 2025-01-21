from ..models.task import Task

def calculate_kpi():
    total_tasks = Task.objects.count()
    completed_tasks = Task.objects.filter(completed=True).count()
    kpi = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0
    return kpi