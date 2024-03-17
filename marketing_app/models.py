from django.db import models
from django.contrib.auth.models import User

from client_app.models import Client

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    objectives = models.TextField()
    timeline = models.DurationField()

    def __str__(self):
        return self.name



class Campaign(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    milestones = models.TextField(blank=True, null=True)
    deliverables = models.TextField(blank=True, null=True)
    performance_metrics = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.client.user.username} - {self.service.name}"
class Content(models.Model):
    TYPE_CHOICES = (
        ('text', 'Text'),
        ('image', 'Image'),
        ('video', 'Video'),
    )
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('reviewed', 'Reviewed'),
        ('approved', 'Approved'),
    )
    content_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    content_body = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    publication_date = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contents_created')
    reviewed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contents_reviewed', blank=True, null=True)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contents_approved', blank=True, null=True)

    def __str__(self):
        return f"{self.content_type} - {self.status}"
    
class Schedule(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    platform = models.CharField(max_length=100)
    posting_time = models.DateTimeField()

    def __str__(self):
        return f"{self.content.content_type} - {self.platform} - {self.posting_time}"
    
class Booking(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)