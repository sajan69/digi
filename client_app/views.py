from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login,authenticate
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from client_app.forms import ClientForm, ContentStatusForm, LoginForm, UserForm, ClientRegistrationForm, ClientProfileForm
from marketing_app.models import Booking, Campaign, Content, Service
from .models import Client

@login_required
def client_profile(request):
    user = request.user
    client = Client.objects.filter(user=user).first()
    return render(request, 'client_app/client_profile.html', {'user': user, 'client': client})

def client_registration(request):
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            return redirect('client_app:client_profile')
    else:
        form = ClientRegistrationForm()
    return render(request, 'client_app/client_registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('marketing_app:index')  # Redirect to dashboard or any other desired page
    else:
        form = LoginForm()
    return render(request, 'client_app/login.html', {'form': form})

@login_required
def client_management(request):
    clients = Client.objects.all()
    return render(request, 'client_app/client_management.html', {'clients': clients})

@login_required
def client_update(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=client.user)
        client_form = ClientForm(request.POST, instance=client)
        if user_form.is_valid() and client_form.is_valid():
            user_form.save()
            client_form.save()
            return redirect('client_app:client_profile')
    else:
        user_form = UserForm(instance=client.user)
        client_form = ClientForm(instance=client)
    return render(request, 'client_app/client_update.html', {
        'user_form': user_form,
        'client_form': client_form,
    })

@login_required
def client_delete(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST':
        user = client.user
        client.delete()
        user.delete()
        return redirect('client_app:client_management')
    return render(request, 'client_app/client_delete.html', {'client': client})

def logout_view(request):
    logout(request)
    return redirect('marketing_app:index')




def all_bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'client_app/all_bookings.html', {'bookings': bookings})

def all_contents(request):
    contents = Content.objects.all()
    return render(request, 'client_app/all_contents.html', {'contents': contents})

def change_content_status(request, content_id):
    content = get_object_or_404(Content, pk=content_id)
    if request.method == 'POST':
        form = ContentStatusForm(request.POST, instance=content)
        if form.is_valid():
            form.save()
            return redirect('client_app:all_contents')
    else:
        form = ContentStatusForm(instance=content)
    return render(request, 'client_app/all_contents.html', {'form': form})

from django.shortcuts import render
from django.db.models import Count
from django.http import JsonResponse





def analytics_view(request):
    
    service_usage = Service.objects.annotate(booking_count=Count('booking'))

    service_names = [service.name for service in service_usage]
    booking_counts = [service.booking_count for service in service_usage]

   
    clients_per_service = [Booking.objects.filter(service=service).values('user').distinct().count() for service in service_usage]

    return render(request, 'client_app/analytics.html', {'service_names': service_names, 'booking_counts': booking_counts, 'clients_per_service': clients_per_service})
