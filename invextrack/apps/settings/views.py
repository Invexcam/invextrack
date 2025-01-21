from django.shortcuts import render
from django.http import HttpResponse

# Vue basée sur une fonction
def settings_home(request):
    return render(request, 'settings/home.html')

# Vue basée sur une classe
from django.views import View

class SettingsView(View):
    def get(self, request):
        return render(request, 'settings/home.html')