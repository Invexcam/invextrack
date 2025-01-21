from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.file import File
from ..serializers.file_serializer import FileSerializer

class FileView(APIView):
    def get(self, request):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)