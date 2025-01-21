from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.label import Label
from ..serializers.label_serializer import LabelSerializer

class LabelView(APIView):
    def get(self, request):
        labels = Label.objects.all()
        serializer = LabelSerializer(labels, many=True)
        return Response(serializer.data)