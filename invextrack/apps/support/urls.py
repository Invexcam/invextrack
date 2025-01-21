from django.urls import path
from .views import TicketView, ReplyView, CategoryView

urlpatterns = [
    path('tickets/', TicketView.as_view(), name='ticket-list'),
    path('replies/', ReplyView.as_view(), name='reply-list'),
    path('categories/', CategoryView.as_view(), name='category-list'),
]