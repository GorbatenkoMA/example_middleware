from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(LoginRequiredMixin, TemplateView):

    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
