# coding=utf-8
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from core.models import Controle


class Perfil(Controle):
    avatar = models.ImageField(upload_to='imagens/usuario', null=True, blank=True,
                               default='imagens/usuario/no-image.jpg', width_field="width_field",
                               height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    usuario = models.OneToOneField(User, related_name='perfil')

    class Meta:
        verbose_name_plural = 'Perfis'

    def __str__(self):
        return self.avatar.url


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, **kwargs):
    if kwargs.get('created', False):
        Perfil.objects.get_or_create(usuario=kwargs.get('instance'))
