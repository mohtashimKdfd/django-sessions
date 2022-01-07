from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    createdAT = models.TimeField(auto_now_add=True)
    updatedAt = models.TimeField(auto_now=True)

    def __str__(self):
        return self.username

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Users,default=None,on_delete=CASCADE)    

    def __str__(self) -> str:
        return self.name

#uuid
#serial id