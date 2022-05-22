from ftplib import MAXLINE
from urllib.parse import MAX_CACHE_SIZE
from django.db import models


'''Se crea la bbdd con los datos requeridos para cumplimentar el entregable, a ser
datos de tipo: Char, Integer y Date
'''
class BdFamilia(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    fechaNacimiento = models.DateField()
    