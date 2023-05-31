import uuid

from django.db import models

from users.models import *


class Blog(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=False, null=False)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # featured_image = models.ImageField(default='blogs/default.jpg')
    title = models.CharField(max_length=500, blank=False, null=False)
    description = models.TextField(null=True, blank=True)
    content = models.TextField(blank=False, null=False)
    keyword = models.CharField(max_length=200, blank=True, null=True)
    upvote = models.IntegerField(default=0, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
