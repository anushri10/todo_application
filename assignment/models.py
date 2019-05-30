from django.db import models
import datetime
from django.utils import timezone

PRIORITY_CHOICES = ( (1, 'Low'), (2, 'Normal'), (3, 'High'), )

class User(models.Model):
 fname = models.CharField(max_length=255)
 lname= models.CharField(max_length=255)
 email=models.EmailField(max_length=255,unique=True)
 password = models.CharField(max_length=200)
 join_date=models.DateTimeField(editable=False,default=timezone.now())
 
 def __str__(self): 
    return self.fname 
 class Meta: 
    ordering = ['join_date'] 


class Todo(models.Model):
  todo_job= models.TextField(max_length=255)
  priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2) 
  completed = models.BooleanField(default=False)
  user=models.ForeignKey('User',on_delete=models.CASCADE,)
  created_date=models.DateTimeField(editable=False,default=timezone.now())
    
  def __str__(self): 
    return self.todo_job
  class Meta: 
    ordering = ['-priority'] 
