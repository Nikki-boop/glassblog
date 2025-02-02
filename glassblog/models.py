from django.db import models
from django.utils.timezone import now

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    date_posted = models.DateTimeField(default=now)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title

# Create your models here.
