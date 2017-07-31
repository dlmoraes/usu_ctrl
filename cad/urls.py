#coding=utf-8

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.FuncionariosNaoMapeadosTemplate.as_view(), name='usuarios'),
    url(r'^negociadores_mapeados/$', views.FuncionariosMapeadosTemplate.as_view(), name='negoc_map'),
    url(r'^nao_map_usus/$', views.FuncionariosNaoMapeadosJson.as_view(), name='nao_map_usu_json'),
    url(r'^map_usus/$', views.FuncionariosMapeadosJson.as_view(), name='map_usu_json'),
    url(r'^canal_select/$', views.CanalSelectJson.as_view(), name='canal_json'),
    url(r'^regional_select/$', views.RegionalSelectJson.as_view(), name='regional_json'),
    url(r'^atl_negociador/(?P<pk>\d+)/$', views.FuncionarioEditAjax.as_view(), name='atualizar_negc_json'),
]
