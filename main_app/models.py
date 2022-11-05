from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    content = models.CharField(max_length=5000)
    author = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title}: {self.description}\r\n{self.content}\r\n Authored by: {self.author}"