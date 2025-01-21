from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from calendar.views import EventViewSet
from integrations.views import IntegrationViewSet
from themes.views import ThemeViewSet
from .views import settings_home, SettingsView

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('events', EventViewSet)
router.register('integrations', IntegrationViewSet)
router.register('themes', ThemeViewSet)

urlpatterns = [
    path('', settings_home, name='settings_home'),
    path('class/', SettingsView.as_view(), name='settings_class_view'),
    path('api/', include(router.urls)),  # Inclure les routes de l'API REST
]