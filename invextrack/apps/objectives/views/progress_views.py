from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.progress import Progress
from ..serializers.progress_serializer import ProgressSerializer

class ProgressView(APIView):
    def get(self, request):
        progress_entries = Progress.objects.all()
        serializer = ProgressSerializer(progress_entries, many=True)
        return Response(serializer.data)