from ..models.analytics import Analytics

def aggregate_data():
    # Example aggregation logic
    data = Analytics.objects.all()
    aggregated_data = {}
    for item in data:
        aggregated_data[item.name] = item.data
    return aggregated_data