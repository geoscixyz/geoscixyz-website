from django.db import models

class Site(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default='')
    url = models.TextField()
    updatedLast = models.DateTimeField()
    updatedLastBy = models.TextField(default='')