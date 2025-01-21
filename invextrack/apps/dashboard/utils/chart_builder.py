import json

def build_chart(data):
    # Example chart building logic
    chart_data = {
        'type': 'bar',
        'data': data,
    }
    return json.dumps(chart_data)