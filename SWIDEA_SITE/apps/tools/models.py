from django.db import models

class Tool(models.Model):
    name = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)