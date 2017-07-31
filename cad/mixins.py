#coding=utf-8
#encoding=utf-8

import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from .models import Funcionario, RegionalCanal, Canal

class FuncionariosNaoMapeadosJsonMixin(object):

    def render_to_response(self, context):
        if self.request.is_ajax():
            queryset = Funcionario.objects.filter(canal__isnull=True)\
                        .values('pk', 'login', 'nome')
            return JsonResponse({
                "data": list(queryset)
            })
        else:
            return {}

class FuncionariosMapeadosJsonMixin(object):

    def render_to_response(self, context):
        if self.request:
            queryset = Funcionario.objects.select_related('canal', 'regional').filter(canal__isnull=False)
            dados = []
            for d in queryset:
                dados.append({
                    'pk': d.pk,
                    'login': d.login,
                    'nome': d.nome,
                    'canal': d.canal.nome,
                    'regional': d.regional.nome
                })
            return JsonResponse({
                "data": dados
            })
        else:
            return {}

class CanalSelectJsonMixin(object):

    def render_to_response(self, context):
        if self.request.is_ajax():
            queryset = Canal.objects.all().values('nome', 'pk').exclude(nome__contains='Izzy')
            return JsonResponse({ 'canais': list(queryset) })


class RegionalSelectJsonMixin(object):

    def render_to_response(self, context):
        if self.request.is_ajax():
            queryset = RegionalCanal.objects.all().values('nome', 'pk')
            return JsonResponse({ 'regionais': list(queryset) })

class FormInvalidAjaxableResponseMixin(object):
    def form_invalid(self, form):
        response = super(FormInvalidAjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

class FormSuccessAjaxableResponseMixin(object):
    def get_success_url(self):
        return JsonResponse({}, status=200)


class FuncionarioAjaxableResponseMixin(FormInvalidAjaxableResponseMixin, FormSuccessAjaxableResponseMixin, object):
    def form_valid(self, form):
        response = super(FuncionarioAjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk
            }
            return JsonResponse(data)
        else:
            return response
