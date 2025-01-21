from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.task import Task
from ..serializers.task_serializer import TaskSerializer

class TaskView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)