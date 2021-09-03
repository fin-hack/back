from django.db import models
from django.contrib.auth.models import User



class OpUser(models.Model):
    mail = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    score = models.IntegerField()
    money = models.IntegerField()
    token = models.CharField(max_length=255)

    def create(self):
        pass


class Achievement(models.Model):
    name = models.CharField(max_length=250)
    user = models.ForeignKey("OpUser", on_delete=models.CASCADE)
