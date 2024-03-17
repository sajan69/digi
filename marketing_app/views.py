from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Service, Content
from .forms import BookingForm,  ContentForm, ScheduleForm, ServiceAddForm, ServiceUpdateForm


from django.contrib import messages
def index(request):
    return render(request, 'marketing_app/index.html')

@login_required
def service_list(request):
    services = Service.objects.all()
    return render(request, 'marketing_app/service_list.html', {'services': services})

@login_required
def service_detail(request, service_id):
    service = get_object_or_404(Service, pk=service_id)

    update_form = None
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            update_form = ServiceUpdateForm(request.POST, instance=service)
            if update_form.is_valid():
                update_form.save()
                messages.success(request, 'Service updated successfully!')
        else:
            update_form = ServiceUpdateForm(instance=service)

    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.service = service  
            booking.user = request.user  
            booking.save()
            messages.success(request, 'Service booked successfully!')
            return redirect('marketing_app:service_detail', service_id=service_id)
    else:
        form = BookingForm()
    
    return render(request, 'marketing_app/service_detail.html', {'service': service, 'form': form, 'update_form': update_form})
@login_required
def content_list(request):
    contents = Content.objects.filter(created_by=request.user)
    return render(request, 'marketing_app/content_list.html', {'contents': contents})

@login_required
def content_create(request):
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            content = form.save(commit=False)
            content.created_by = request.user
            content.save()
            return redirect('marketing_app:content_list')
    else:
        form = ContentForm()
    return render(request, 'marketing_app/content_create.html', {'form': form})

@login_required
def content_detail(request, content_id):
    content = get_object_or_404(Content, pk=content_id)
    if request.method == 'POST':
        form = ContentForm(request.POST, instance=content)
        if form.is_valid():
            form.save()
            return redirect('marketing_app:content_detail', content_id=content.id)
    else:
        form = ContentForm(instance=content)
    return render(request, 'marketing_app/content_detail.html', {'content': content, 'form': form})


@login_required
def content_schedule(request, content_id):
    content = get_object_or_404(Content, pk=content_id)
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.content = content
            schedule.save()
            return redirect('marketing_app:content_detail', content_id=content.id)
    else:
        form = ScheduleForm()
    return render(request, 'marketing_app/content_schedule.html', {'content': content, 'form': form})

def add_service(request):
    print(request.POST)

    if request.method == 'POST':
        form = ServiceAddForm(request.POST)
        if form.is_valid():
            service_instance = form.save()
            print(service_instance) 
            return redirect('marketing_app:service_list')
    else:
        print(form.errors)
    return render(request, 'marketing_app/service_list.html', {'form': form})
