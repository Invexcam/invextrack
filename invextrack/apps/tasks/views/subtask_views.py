from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.subtask import Subtask
from ..serializers.subtask_serializer import SubtaskSerializer

class SubtaskView(APIView):
    def get(self, request):
        subtasks = Subtask.objects.all()
        serializer = SubtaskSerializer(subtasks, many=True)
        return Response(serializer.data)