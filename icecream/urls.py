from django.urls import path

from . import views

app_name = 'icecream'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),
    path('add/', views.CreateView.as_view(), name = 'create'),
]