from django.urls import path

from . import views

app_name = 'icecream'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),
    path('add/', views.CreateView.as_view(), name = 'create'),
    path('daily_flavors/', views.DailyFlavorView.as_view(), name = 'daily_flavors'),
    path('weekly_flavors/', views.WeeklyFlavorView.as_view(), name = 'weekly_flavors'),
    path('seasonal_flavors/', views.SeasonalFlavorView.as_view(), name = 'seasonal_flavors'),
    path('featured_flavors/', views.FeaturedFlavorView.as_view(), name = 'featured_flavors'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name = 'delete'),
    path('<int:pk>/update/', views.UpdateView.as_view(), name = 'update'),

]