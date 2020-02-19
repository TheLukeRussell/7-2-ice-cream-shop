from django.views import generic
from django.urls import reverse_lazy
from django.conf import settings

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

class DeleteView(generic.DeleteView):
    template_name = 'icecream/delete.html'
    model = Icecream
    success_url = reverse_lazy('icecream/detail.html')

class UpdateView(generic.UpdateView):
    template_name = 'icecream/update.html'
    model = Icecream
    fields = '__all__'

class DailyFlavorView(generic.ListView):
    template_name = 'icecream/daily_flavors.html'
    model = Icecream
    queryset = Icecream.objects.filter(available='Daily')

class WeeklyFlavorView(generic.ListView):
    template_name = 'icecream/weekly_flavors.html'
    model = Icecream
    queryset = Icecream.objects.filter(available='Weekly')

class SeasonalFlavorView(generic.ListView):
    template_name = 'icecream/seasonal_flavors.html'
    model = Icecream
    queryset = Icecream.objects.filter(available='Seasonal')

class FeaturedFlavorView(generic.ListView):
    template_name = 'icecream/featured_flavors.html'
    model = Icecream
    queryset = Icecream.objects.filter(Featured=True)
