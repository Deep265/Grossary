from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class SignUp(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="prof",null=True)
    image = models.ImageField(upload_to="profile_photos/",null=True)
    phone = models.CharField(blank=True,max_length=50)
    age = models.CharField(blank=True,max_length=5)
    address = models.TextField(blank=True)

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    subject = models.TextField(blank=True)
    message = models.TextField(blank=True)

