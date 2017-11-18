# Import bits of code from other files
from django.db import models
from django.utils import timezone


# Define our model (Django will save it in a database)
class Post(models.Model):
    author = models.ForeignKey('auth.User')     # a link to another model
    title = models.CharField(max_length = 200)  # text with limited characters
    text = models.TextField()                   # long text with no limit
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now
        self.save()
    
    def __str_(self):
        return self.title