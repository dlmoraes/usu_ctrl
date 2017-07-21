#coding=utf-8
from django.db import models

from core.models import Controle

# Create your models here.
class MacroCanal(Controle):
    nome = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Macro Canal'
        verbose_name_plural = 'Macro Canais'
        ordering = ['nome',]

    def __str__(self):
        return self.nome

class Canal(Controle):
    nome = models.CharField(max_length=50, unique=True)
    macro = models.ForeignKey('MacroCanal', related_name='macros')

    class Meta:
        verbose_name_plural = 'Canais'
        ordering = ['nome',]

    def __str__(self):
        return self.nome 

class RegionalCanal(Controle):
    nome = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = 'Regionais'
        ordering = ['nome',]

    def __str__(self):
        return self.nome 

class Funcionario(Controle):
    login = models.CharField(max_length=15, unique=True)
    nome = models.CharField(max_length=60)
    canal = models.ForeignKey('Canal', related_name='canais')
    regional = models.ForeignKey('RegionalCanal', related_name='regionais')
    is_ativo = models.BooleanField('situação', default=True)
    
    class Meta:
        ordering = ['login',]

    def __str__(self):
        return self.login
    
