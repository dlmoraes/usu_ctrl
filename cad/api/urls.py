from django.conf.urls import url
from django.contrib import admin

from .views import (
    MacroCanalViewSet
    )

urlpatterns = [
    url(r'^$', MacroCanalViewSet.as_view(), name='list'),
]
