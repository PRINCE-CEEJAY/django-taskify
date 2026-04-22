from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('title', 'user')