#coding=utf-8

from django.db import models

# Create your models here.
class Controle(models.Model):
    dt_criado = models.DateTimeField('criado em', auto_now=False, auto_now_add=True)
    dt_modificado = models.DateTimeField('modificado em', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
