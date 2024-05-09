from django.db import models

# Create your models here.
class bokeyou(models.Model):
    substance =models.CharField(max_length=250)
    url =models.CharField(max_length=250)
    author =models.CharField(max_length=250)

