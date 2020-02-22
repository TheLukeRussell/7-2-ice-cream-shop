from django.shortcuts import render
from django.views import generic

class IndexView(generic.TemplateView):
    template_name = 'index.html'

class AboutView(generic.TemplateView):
    template_name = 'about.html'

class ContactUsView(generic.TemplateView):
    template_name = 'contact_us.html'
