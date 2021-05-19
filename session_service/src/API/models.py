from django.db import models


class User(models.Model):
    uid = models.UUIDField(primary_key=True)
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False)
