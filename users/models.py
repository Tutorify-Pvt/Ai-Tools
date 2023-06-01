import uuid

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, null=False, blank=False)
    username = models.CharField(max_length=250, null=False, blank=False)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=400, null=False, blank=False)
    location = models.CharField(max_length=200, null=True, blank=True)
    short_intro = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    social_github = models.CharField(max_length=200, null=True, blank=True)
    social_twitter = models.CharField(max_length=200, null=True, blank=True)
    social_website = models.CharField(max_length=200, null=True, blank=True)
    role = models.ManyToManyField('Role', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Role(models.Model):
    id = models.UUIDField(default= uuid.uuid4, primary_key=True, editable=False, null=False, blank=False)
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title