from django.db import models

class Item(models.Model):
    ip = models.CharField(max_length=256, primary_key=True)
    status = models.CharField(max_length=32)
