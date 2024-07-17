from django.db import models
from apps.tools.models import Tool

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='reviews_images/', blank=True, null=True)
    content = models.TextField()
    interest = models.CharField(max_length=100, blank=True, null=True)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name='posts')
    idea_star = models.BooleanField(default=False)