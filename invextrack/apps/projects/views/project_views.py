from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.project import Project
from ..serializers.project_serializer import ProjectSerializer

class ProjectView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)