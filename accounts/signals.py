from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwarge):
    if created:
        user = instance
        profile1 = Profile.objects.create(
            user=user,
        )