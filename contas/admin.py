#coding=utf-8
from django.contrib import admin

from .models import Perfil

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):

    list_display = ['usuario', 'height_field', 'width_field', 'avatar',]
