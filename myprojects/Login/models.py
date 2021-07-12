from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Login(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=50)
    usertype = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'login1'
