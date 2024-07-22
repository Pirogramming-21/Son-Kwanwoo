from django.db import models

class Post(models.Model):
    like = models.IntegerField(default=0)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"Post {self.id}"