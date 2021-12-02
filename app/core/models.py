from django.db import models


class Video(models.Model):
    """Custom Video Model for storing Video Data"""
    vid = models.CharField(null=False, blank=False, max_length=1000)
    title = models.CharField(null=True, blank=True, max_length=1000)
    description = models.CharField(null=True, blank=True, max_length=10000)
    publishing_datetime = models.DateTimeField()
    thumbnail_URLs = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
