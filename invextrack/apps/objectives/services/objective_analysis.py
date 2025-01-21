from ..models.progress import Progress

def analyze_objective_progress(objective):
    progress_entries = Progress.objects.filter(objective=objective)
    total_progress = sum(entry.progress_value for entry in progress_entries)
    return total_progress / len(progress_entries) if progress_entries else 0