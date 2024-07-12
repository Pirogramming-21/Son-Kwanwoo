from django.db import models

class Reviews(models.Model):
    genre_choices = [
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Animation', 'Animation'),
        ('Comedy', 'Comedy'),
        ('Crime', 'Crime'),
        ('Documentary', 'Documentary'),
        ('Drama', 'Drama'),
        ('Family', 'Family'),
        ('Fantasy', 'Fantasy'),
        ('Horror', 'Horror'),
        ('Musical', 'Musical'),
        ('Romance', 'Romance'),
        ('SF', 'SF'),
        ('Sport', 'Sport'),
        ('Thriller', 'Thriller'),
    ]
    
    title = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    genre = models.CharField(max_length=50, choices=genre_choices)
    rank = models.PositiveIntegerField()
    director = models.CharField(max_length=50)
    actor = models.CharField(max_length=100)
    running_time = models.PositiveIntegerField()
    content = models.TextField()

    def __str__(self):
        return self.title