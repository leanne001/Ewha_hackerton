from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib import auth
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    studentid = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    menu = models.TextField(max_length=100)

@receiver(post_save, sender=User)
def create_user_profile(sender , instance, created, **kwargs) :
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender = User)
def save_user_profile(sender, instance, **kwargs) :
    instance.profile.save()