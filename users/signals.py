from django.db.models.signals import *
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=User)
def profile_creation(sender, instance, **kwargs):
    if kwargs['created']:
        Profile.objects.create(
            owner=instance,
            username=instance.username,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email
        )


@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    instance.owner.delete()
