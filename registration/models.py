from django.db import models
from django.db.models import EmailField, CharField, Model
class user_data(models.Model):
    user_name =models.CharField(max_length=100)
    user_mobile=models.CharField(max_length=10)
    user_email= models.EmailField(max_length=100)
# Create your models here.
