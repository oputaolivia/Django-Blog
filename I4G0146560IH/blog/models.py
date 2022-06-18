from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(User, default = None, null= True, on_delete=models.SET_NULL)
    Created_date = models.DateTimeField(auto_now_add=True)
    Published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.Title
        