from django.urls import path
from .views import ProjectView, TaskView, CommentView, FileView

urlpatterns = [
    path('projects/', ProjectView.as_view(), name='project-list'),
    path('tasks/', TaskView.as_view(), name='task-list'),
    path('comments/', CommentView.as_view(), name='comment-list'),
    path('files/', FileView.as_view(), name='file-list'),
]