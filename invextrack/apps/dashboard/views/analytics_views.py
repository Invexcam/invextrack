from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.analytics import Analytics
from ..serializers.analytics_serializer import AnalyticsSerializer

class AnalyticsView(APIView):
    def get(self, request):
        analytics = Analytics.objects.all()
        serializer = AnalyticsSerializer(analytics, many=True)
        return Response(serializer.data)