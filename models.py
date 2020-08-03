from django.db import models
from django.utils import timezone

# Create your models here.
class TodoListItem(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField() 
    date = models.DateTimeField(default=timezone.now)

   