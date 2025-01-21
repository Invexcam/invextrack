import os
import django
from django.conf import settings
from django.urls import get_resolver, URLPattern, URLResolver

# Configurez les paramètres Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'invextrack.settings')
django.setup()

def list_urls(lis, acc=''):
    for entry in lis:
        if isinstance(entry, URLPattern):
            print(acc + str(entry.pattern))
        elif isinstance(entry, URLResolver):
            print(acc + str(entry.pattern))
            list_urls(entry.url_patterns, acc + str(entry.pattern))

def show_urls():
    urlconf = settings.ROOT_URLCONF
    resolver = get_resolver(urlconf)
    list_urls(resolver.url_patterns)

if __name__ == "__main__":
    show_urls()