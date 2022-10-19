from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=20)
    phone=models.IntegerField()
    email=models.EmailField()
    message=models.CharField(max_length=15)
    address=models.CharField(max_length=50)
