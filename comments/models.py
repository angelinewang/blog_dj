from django.db import models
from blogs.models import Blog
from users.models import User

# Create your models here.

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField(max_length=500, default='')