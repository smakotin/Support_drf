from django.urls import path

from .views import TicketsListAPIView

urlpatterns = [
    path('tickets/', TicketsListAPIView.as_view()),
]
