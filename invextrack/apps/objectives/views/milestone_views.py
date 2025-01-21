from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.milestone import Milestone
from ..serializers.milestone_serializer import MilestoneSerializer

class MilestoneView(APIView):
    def get(self, request):
        milestones = Milestone.objects.all()
        serializer = MilestoneSerializer(milestones, many=True)
        return Response(serializer.data)