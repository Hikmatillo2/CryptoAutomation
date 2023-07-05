from django.db import models


class BotUser(models.Model):
    username = models.CharField()