import uuid

from django.db import models

from users.models import *

class Tag(models.Model):
    id = models.UUIDField(default= uuid.uuid4, primary_key=True, editable=False, null=False, blank=False)
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Type(models.Model):
    id = models.UUIDField(default= uuid.uuid4, primary_key=True, editable=False, null=False, blank=False)
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Directory(models.Model):
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, null=False, blank=False)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    features = models.TextField(null=True, blank=True)
    # featured_image = models.ImageField(null=True, blank=True, default="directory/default.jpg")
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField('Tag', blank=True)
    types = models.ManyToManyField('Type', blank=True)
    active = models.BooleanField(null=True, blank=True)
    def __str__(self):
        return self.title


