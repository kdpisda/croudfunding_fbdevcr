from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Campaign(models.Model):
    title = models.CharField(max_length=32, null=False, blank=False)
    description = models.TextField()
    amount = models.FloatField(default=1, null=False, blank=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    approved = models.BooleanField(default=False)
    supporting_document = models.FileField(upload_to="uploads/campaigns", null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Supporter(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.FloatField(default=1, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)