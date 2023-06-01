from django.dispatch import receiver
from django.db.models.signals import *
from .models import *
import ast

@receiver(post_save, sender=Directory)
def update_features(sender, instance, **kwargs):
    feature = list(filter(lambda x: x, map(lambda x: x.strip() if x.strip() else None, instance.features.split('|'))))
    print(feature)
    if feature and type(ast.literal_eval(instance.features)) is not list:
        Directory.objects.filter(id=instance.id).update(features=feature)
    print(instance.id)



    # list(filter(lambda x: x, map(lambda x: x.strip() if x.strip() else None, directory.features.split('|'))))
