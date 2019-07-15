from django.views.generic import TemplateView
from django.shortcuts import render


class indexView(TemplateView):
    template_name = "index.html"
