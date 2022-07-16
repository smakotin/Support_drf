from rest_framework.routers import SimpleRouter
from tickets.views import TicketViewSet


router = SimpleRouter()
router.register(r'tickets', TicketViewSet)
urlpatterns = router.urls
