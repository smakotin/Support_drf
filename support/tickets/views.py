from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from tickets.models import Ticket
from tickets.serializers import TicketSerializer


class TicketsListAPIView(ListAPIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]
    queryset = Ticket.objects.all()
