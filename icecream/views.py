from django.views import generic

from .models import Icecream

class IndexView(generic.ListView):
    template_name = 'icecream/index.html'
    model = Icecream
