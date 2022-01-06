from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    createdAT = models.TimeField(auto_now_add=True)
    updatedAt = models.TimeField(auto_now=True)

    def __str__(self):
        return self.username