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

from .serializers import MacroCanalSerializer


class MacroCanalViewSet(ListAPIView):
    serializer_class = MacroCanalSerializer