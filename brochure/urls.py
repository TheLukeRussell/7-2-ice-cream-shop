from django.urls import path

from . import views

app_name = 'brochure'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('about/', views.AboutView.as_view(), name = 'about'),
    path('contact/', views.ContactUsView.as_view(), name = 'contact')
]