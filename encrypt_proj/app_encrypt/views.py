# from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'


class EncryptView(TemplateView):
    template_name = 'encrypt.html'


class DecryptView(TemplateView):
    template_name = 'decrypt.html'
