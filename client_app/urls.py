from django.urls import path
from . import views

app_name = 'client_app'

urlpatterns = [
    path('register/', views.client_registration, name='client_registration'),
    path('profile/', views.client_profile, name='client_profile'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('clients/', views.client_management, name='client_management'),
    path('clients/<int:client_id>/update/', views.client_update, name='client_update'),
    path('clients/<int:client_id>/delete/', views.client_delete, name='client_delete'),
    path('all-bookings/', views.all_bookings, name='all_bookings'),
    path('all-contents/', views.all_contents, name='all_contents'),
    path('change-content-status/<int:content_id>/', views.change_content_status, name='change_content_status'),
    path('analytics/', views.analytics_view, name='analytics'),
]