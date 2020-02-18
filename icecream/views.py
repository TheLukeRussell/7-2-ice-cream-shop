from django.views import generic

from .models import Icecream

class IndexView(generic.ListView):
    template_name = 'icecream/index.html'
    model = Icecream

class DetailView(generic.DetailView):
    template_name = 'icecream/detail.html'
    model = Icecream

class CreateView(generic.CreateView):
    template_name = 'icecream/create.html'
    model = Icecream
    fields = '__all__'
