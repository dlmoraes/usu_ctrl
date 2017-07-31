#coding=utf-8

from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
)
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView, 
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)

from .serializers import (
    CanalSerializer,
    CanalSelectSerializer,
    FuncionarioSerializer,
    MacroCanalSerializer,
    MacroCanalSelectSerializer,
    RegionalSerializer,
    RegionalSelectSerializer
)
from cad.models import Canal, Funcionario, MacroCanal, RegionalCanal

class CanalViewSet(ListAPIView):
    serializer_class = CanalSerializer

    def get_queryset(self, *args, **kwargs):
        list = Canal.objects.all()
        return list

class CanalSelectViewSet(ListAPIView):
    serializer_class = CanalSelectSerializer

    def get_queryset(self, *args, **kwargs):
        list = Canal.objects.all()
        return list

class FuncionarioViewSet(ListAPIView):
    serializer_class = FuncionarioSerializer

    def get_queryset(self, *args, **kwargs):
        list = Funcionario.objects.select_related('canal', 'regional').all()
        return list

class MacroCanalViewSet(ListAPIView):
    serializer_class = MacroCanalSerializer

    def get_queryset(self, *args, **kwargs):
        list = MacroCanal.objects.all()
        return list

class MacroCanalSelectViewSet(ListAPIView):
    serializer_class = MacroCanalSelectSerializer

    def get_queryset(self, *args, **kwargs):
        list = MacroCanal.objects.all()
        return list

class RegionalViewSet(ListAPIView):
    serializer_class = RegionalSerializer

    def get_queryset(self, *args, **kwargs):
        list = RegionalCanal.objects.all()
        return list


class RegionalSelectViewSet(ListAPIView):
    serializer_class = RegionalSelectSerializer

    def get_queryset(self, *args, **kwargs):
        list = RegionalCanal.objects.all()
        return list