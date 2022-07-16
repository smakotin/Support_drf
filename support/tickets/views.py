from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

from tickets.models import Ticket
from tickets.serializers import TicketSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [DjangoModelPermissions]
