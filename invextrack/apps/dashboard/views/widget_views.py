from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.widget import Widget
from ..serializers.widget_serializer import WidgetSerializer

class WidgetView(APIView):
    def get(self, request):
        widgets = Widget.objects.all()
        serializer = WidgetSerializer(widgets, many=True)
        return Response(serializer.data)