from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from . import views  # Assurez-vous que votre vue est correctement importée

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('apps.tasks.urls')),
    path('objectives/', include('apps.objectives.urls')),
    path('projects/', include('apps.projects.urls')),
    path('dashboard/', include('apps.dashboard.urls')),
    path('support/', include('apps.support.urls')),
    path('settings/', include('apps.settings.urls')),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),

    # Redirection vers la vue personnalisée pour les pages non définies
    path('', views.custom_error_page),  # URL par défaut
]