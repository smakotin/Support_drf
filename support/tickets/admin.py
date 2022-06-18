from django.contrib import admin
from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_filter = ('status',)
    list_display = ('id', 'title', 'status', 'description')
    list_editable = ('status',)
