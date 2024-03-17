from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking, Campaign, Client, Service, Content, Schedule


class ServiceAddForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'objectives', 'timeline']
        
class ServiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'objectives', 'timeline']


        

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ('content_type', 'content_body', 'publication_date')
        widgets = {
            'publication_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            
        }

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('platform', 'posting_time')
        widgets = {
            'posting_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            
        }

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['service', 'start_date', 'end_date', 'milestones', 'deliverables', 'performance_metrics']
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'email', 'phone_number']