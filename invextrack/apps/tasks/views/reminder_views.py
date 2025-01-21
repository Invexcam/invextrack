from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.notification import Notification
from ..serializers.notification_serializer import NotificationSerializer

class ReminderView(APIView):
    def get(self, request):
        reminders = Notification.objects.all()
        serializer = NotificationSerializer(reminders, many=True)
        return Response(serializer.data)