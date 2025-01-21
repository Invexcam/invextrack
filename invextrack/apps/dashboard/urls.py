from django.urls import path
from .views import DashboardView, WidgetView, AnalyticsView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('widgets/', WidgetView.as_view(), name='widget-list'),
    path('analytics/', AnalyticsView.as_view(), name='analytics-list'),
]