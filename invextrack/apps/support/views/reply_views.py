from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.reply import Reply
from ..serializers.reply_serializer import ReplySerializer

class ReplyView(APIView):
    def get(self, request):
        replies = Reply.objects.all()
        serializer = ReplySerializer(replies, many=True)
        return Response(serializer.data)