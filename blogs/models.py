from django.db import models
from users.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    content = models.CharField(max_length=5000)
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title