from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.ticket import Ticket
from ..serializers.ticket_serializer import TicketSerializer

class TicketView(APIView):
    def get(self, request):
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)