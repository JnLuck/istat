from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import CertificadoModular
# Create your views here.

class CertificadoModularList(ListView):
    model = CertificadoModular
    template_name = "certificados/list_cm.html"
    context_object_name = "all_certify"


class CertificadoModularDetail(DetailView):
    model = CertificadoModular
    template_name = "certificados/certificado_modular.html"
    context_object_name = "single_certify"