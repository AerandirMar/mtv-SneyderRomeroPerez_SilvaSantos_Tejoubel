from ftplib import MAXLINE
from urllib.parse import MAX_CACHE_SIZE
from django.db import models


class BdFamilia(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    fechaNacimiento = models.DateField()
    