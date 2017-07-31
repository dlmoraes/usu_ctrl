# coding=utf-8
# encoding=utf-8

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView, UpdateView

from .mixins import (
    CanalSelectJsonMixin,
    FuncionariosNaoMapeadosJsonMixin,
    FuncionariosMapeadosJsonMixin,
    RegionalSelectJsonMixin,
    FuncionarioAjaxableResponseMixin
)
from .models import Funcionario


class FuncionariosNaoMapeadosTemplate(LoginRequiredMixin, TemplateView):
    template_name = 'funcionario/index.html'
    context_object_name = 'funcs'

    def get_context_data(self, **kwargs):
        context = super(FuncionariosNaoMapeadosTemplate, self).get_context_data(**kwargs)
        context['titulo'] = 'Usuários <small>não mapeados</small>'
        return context


class FuncionariosMapeadosTemplate(LoginRequiredMixin, TemplateView):
    template_name = 'funcionario/mapeados.html'
    context_object_name = 'funcs'

    def get_context_data(self, **kwargs):
        context = super(FuncionariosMapeadosTemplate, self).get_context_data(**kwargs)
        context['titulo'] = 'Usuários <small>mapeados</small>'
        return context


class FuncionariosNaoMapeadosJson(LoginRequiredMixin, FuncionariosNaoMapeadosJsonMixin, TemplateView):
    pass

class FuncionariosMapeadosJson(LoginRequiredMixin, FuncionariosMapeadosJsonMixin, TemplateView):
    pass

class CanalSelectJson(LoginRequiredMixin, CanalSelectJsonMixin, TemplateView):
    pass


class RegionalSelectJson(LoginRequiredMixin, RegionalSelectJsonMixin, TemplateView):
    pass


@method_decorator(csrf_protect, name='dispatch')
class FuncionarioEditAjax(LoginRequiredMixin, FuncionarioAjaxableResponseMixin, UpdateView):
    model = Funcionario
    fields = ['canal', 'regional', ]