from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Books(models.Model):
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    bookname = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.CharField(max_length=150, null=True, blank=True)
