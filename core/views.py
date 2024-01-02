from typing import Any, Dict
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Servico, Funcionario, Recurso
from .forms import ContatoForm
from django.utils.translation import gettext as _
from django.utils import translation

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index') #no sucesso vai para index

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs) #recupera o contexto da página index
        #adiciona objetos ao contexto
        lang = translation.get_language()
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['recursos'] = Recurso.objects.order_by('?').all()
        context['lang'] = lang
        translation.activate(lang)
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, _('E-Mail enviado com sucesso')) 
        return super(IndexView,self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _('Erro ao enviar email'))
        return super(IndexView,self).form_invalid(form, *args, **kwargs)       
