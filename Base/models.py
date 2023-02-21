from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    #Using "CASCADE", if the user gets deleted, all the child tasks will be deleted.
    #Using "SET_NULL", the cjhild tasks wont be deleted
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']