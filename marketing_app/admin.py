from django.contrib import admin
from .models import Booking, Service, Content, Campaign, Schedule

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'timeline']

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['content_type', 'status', 'publication_date', 'created_by', 'reviewed_by', 'approved_by']
    list_filter = ['content_type', 'status']
    search_fields = ['content_body', 'created_by__username', 'reviewed_by__username', 'approved_by__username']
    date_hierarchy = 'publication_date'

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ['client', 'service', 'start_date', 'end_date']
    list_filter = ['client', 'service']
    search_fields = ['client__user__username', 'service__name']
    date_hierarchy = 'start_date'

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['content', 'platform', 'posting_time']
    list_filter = ['platform']
    search_fields = ['content__content_body']
    date_hierarchy = 'posting_time'

admin.site.register(Booking)