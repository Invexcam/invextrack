from django.urls import path
from .views import TaskView, SubtaskView, LabelView, ReminderView, DashboardView

urlpatterns = [
    path('tasks/', TaskView.as_view(), name='task-list'),
    path('subtasks/', SubtaskView.as_view(), name='subtask-list'),
    path('labels/', LabelView.as_view(), name='label-list'),
    path('reminders/', ReminderView.as_view(), name='reminder-list'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]