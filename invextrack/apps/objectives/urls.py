from django.urls import path
from .views import ObjectiveView, MilestoneView, ProgressView

urlpatterns = [
    path('objectives/', ObjectiveView.as_view(), name='objective-list'),
    path('milestones/', MilestoneView.as_view(), name='milestone-list'),
    path('progress/', ProgressView.as_view(), name='progress-list'),
]