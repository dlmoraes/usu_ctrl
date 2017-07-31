#coding=utf-8
from django.db import models
from django.urls import reverse_lazy

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

class LocalCanal(Controle):
    nome = models.CharField(max_length=60, unique=True)

    class Meta:
        verbose_name_plural = 'Agências'
        ordering = ['nome', ]

    def __str__(self):
        return self.nome

class Funcionario(Controle):
    login = models.CharField(max_length=15, unique=True)
    nome = models.CharField(max_length=60)
    canal = models.ForeignKey('Canal', related_name='canais', null=True, blank=True)
    regional = models.ForeignKey('RegionalCanal', related_name='regionais', null=True, blank=True)
    is_ativo = models.BooleanField('situação', default=True)
    
    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        ordering = ['login',]

    def __str__(self):
        return self.login

    def get_absolute_url(self):
        return reverse_lazy('cad:atualizar_negc_json', kwargs=dict(pk=self.pk))
    
