#coding=utf-8

from rest_framework.serializers import (
    HyperlinkedIdentityField, ModelSerializer
)

from cad.models import MacroCanal, Canal, RegionalCanal, Funcionario

class FuncionarioSerializer(ModelSerializer):

    class Meta:
        model = Funcionario
        fields = [
            'id',
            'login',
            'nome',
            'is_ativo',
            'canal',
            'regional',
        ]

class MacroCanalSerializer(ModelSerializer):

    class Meta:
        model = MacroCanal
        fields = ['nome',]

class MacroCanalSelectSerializer(ModelSerializer):

    class Meta:
        model = MacroCanal
        fields = ['id', 'nome']

class CanalSerializer(ModelSerializer):

    class Meta:
        model = Canal
        fields = ['nome',]


class CanalSelectSerializer(ModelSerializer):
    class Meta:
        model = Canal
        fields = ['id', 'nome',]


class RegionalSerializer(ModelSerializer):

    class Meta:
        model = RegionalCanal
        fields = ['nome',]


class RegionalSelectSerializer(ModelSerializer):
    class Meta:
        model = RegionalCanal
        fields = ['id', 'nome',]
