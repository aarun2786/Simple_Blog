from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meat:
        ordering = ('-created_at')

    def __str__(self):
        return self.title

class Comments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateField(auto_now=True)


