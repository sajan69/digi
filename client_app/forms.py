from django import forms
from django.contrib.auth.models import User

from marketing_app.models import Content
from .models import Client
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class ClientRegistrationForm(UserCreationForm):
    phone = forms.CharField(max_length=20, required=False)
    marketing_preferences = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        client = Client.objects.create(
            user=user,
            phone=self.cleaned_data['phone'],
            marketing_preferences=self.cleaned_data['marketing_preferences']
        )
        return user
class LoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['phone', 'marketing_preferences']
    
class ClientProfileForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('phone', 'marketing_preferences')



class ContentStatusForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['status']
        labels = {
            'status': 'Status',
        }
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
