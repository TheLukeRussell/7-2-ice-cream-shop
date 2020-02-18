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

class DailyFlavorView(generic.ListView):
    template_name = 'daily_flavors.html'
    model = Icecream
    queryset = Icecream.objects.filter(available='Daily')

class WeeklyFlavorView(generic.ListView):
    template_name = 'weekly_flavors.html'
    model = Icecream
    queryset = Icecream.objects.filter(available='Weekly')

class SeasonalFlavorView(generic.ListView):
    template_name = 'seasonal_flavors.html'
    model = Icecream
    queryset = Icecream.objects.filter(available='Seasonal')

class FeaturedFlavorView(generic.ListView):
    template_name = 'featured_flavors.html'
    model = Icecream
    queryset = Icecream.objects.filter(Featured=True)
