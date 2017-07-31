from django.conf.urls import url
from django.contrib import admin

from .views import (
    CanalViewSet,
    CanalSelectViewSet,
    FuncionarioViewSet,
    MacroCanalViewSet,
    MacroCanalSelectViewSet,
    RegionalViewSet,
    RegionalSelectViewSet
    )

urlpatterns = [
    url(r'^canal/$', CanalViewSet.as_view(), name='canal-list'),
    url(r'^canals/$', CanalSelectViewSet.as_view(), name='canal-select'),
    url(r'^negociadores/$', FuncionarioViewSet.as_view(), name='negociador-list'),
    url(r'^macro/$', MacroCanalViewSet.as_view(), name='macro-list'),
    url(r'^macros/$', MacroCanalSelectViewSet.as_view(), name='macro-select'),
    url(r'^regional/$', RegionalViewSet.as_view(), name='regional-list'),
    url(r'^regionals/$', RegionalSelectViewSet.as_view(), name='regional-select'),
]
