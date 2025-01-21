# filepath: /c:/Users/HP/Documents/App InvexTrack/InvexTrack v.0/invextrack/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('apps.tasks.urls')),
    path('objectives/', include('apps.objectives.urls')),
    path('projects/', include('apps.projects.urls')),
    path('dashboard/', include('apps.dashboard.urls')),
    path('support/', include('apps.support.urls')),
    path('settings/', include('apps.settings.urls')),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
]