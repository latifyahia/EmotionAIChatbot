from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserData(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        emotion = models.CharField(max_length=200)

        def __str__(self):
            return self.emotion





