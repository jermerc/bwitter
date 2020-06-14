from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Callback function for profile creation.
@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Callback function for profile storage into database.
@receiver(post_save, sender=User)
def saveProfile(sender, instance, **kwargs):
    instance.profile.save()