def connect_integration(name, api_key):
    integration = Integration.objects.create(name=name, api_key=api_key)
    return integration