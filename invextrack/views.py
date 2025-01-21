from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def custom_error_page(request):
    """Page d'erreur personnalisée qui s'affiche en cas d'erreur."""
    return HttpResponse('<h1>Bienvenue sur votre application !</h1><p>Tout fonctionne correctement.</p>')

def home(request):
    """Page d'accueil de l'application."""
    return render(request, 'home.html')

def page_not_found(request, exception=None):
    """Page personnalisée pour gérer les erreurs 404."""
    return render(request, '404.html', status=404)