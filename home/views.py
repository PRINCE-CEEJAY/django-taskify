from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = 'example data from python'
        return context