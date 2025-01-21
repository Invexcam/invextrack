from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.comment import Comment
from ..serializers.comment_serializer import CommentSerializer

class CommentView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)