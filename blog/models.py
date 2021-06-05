from django.db import models

# Create your models here.
from .models import * 
from datetime import date
from django.contrib.auth.models import User



class blog(models.Model):
    title=models.CharField(max_length=100,editable=True)
    discrption=models.TextField(max_length=4000)
    dateAdd=models.DateField(auto_created=True)
    image=models.ImageField(upload_to='img/')
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    

    def __str__(self) -> str:
        return self.title