#coding=utf-8

from rest_framework.serializers import (
    HyperlinkedIdentityField, ModelSerializer, SerializerMethod
)

from cad.models import MacroCanal

class MacroCanalSerializer(ModelSerializer):

    class Meta:
        model = MacroCanal
        fields = ['nome',]