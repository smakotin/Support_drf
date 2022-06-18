from django.contrib import admin

from .models import Ticket, TicketMessage


class InlineTicketMessageAdmin(admin.StackedInline):
    model = TicketMessage
    extra = 3


@admin.register(TicketMessage)
class TicketMessageAdmin(admin.ModelAdmin):
    list_filter = ('ticket', 'author')
    list_display = ('id', 'ticket', 'author', 'text', 'created_at')


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_filter = ('status',)
    list_display = ('id', 'title', 'status', 'description', 'created_at')
    list_editable = ('status',)
    inlines = (InlineTicketMessageAdmin,)
