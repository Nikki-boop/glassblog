from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings   


urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
]