from django.urls import path
from . import views

app_name = 'marketing_app'

urlpatterns = [
    path('', views.index, name='index'),
    
    path('services/', views.service_list, name='service_list'),
    path('add-service/', views.add_service, name='add_service'),
    path('services/<int:service_id>/', views.service_detail, name='service_detail'),
    path('content/', views.content_list, name='content_list'),
    path('content/create/', views.content_create, name='content_create'),
    path('content/<int:content_id>/', views.content_detail, name='content_detail'),
    path('content/<int:content_id>/schedule/', views.content_schedule, name='content_schedule'),
]