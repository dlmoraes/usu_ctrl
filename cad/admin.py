#coding=utf-8
from django.contrib import admin

from .models import MacroCanal, Canal, RegionalCanal, Funcionario

@admin.register(MacroCanal)
class MacroCanalAdmin(admin.ModelAdmin):

    list_display = ['nome', 'dt_criado', 'dt_modificado',]

@admin.register(Canal)
class CanalAdmin(admin.ModelAdmin):

    pass

@admin.register(RegionalCanal)
class RegionalCanalAdmin(admin.ModelAdmin):

    pass

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):

    list_display = ['login', 'nome', 'canal', 'regional']