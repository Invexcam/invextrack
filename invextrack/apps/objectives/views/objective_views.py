from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.objective import Objective
from ..serializers.objective_serializer import ObjectiveSerializer

class ObjectiveView(APIView):
    def get(self, request):
        objectives = Objective.objects.all()
        serializer = ObjectiveSerializer(objectives, many=True)
        return Response(serializer.data)