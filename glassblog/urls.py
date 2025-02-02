from django.urls import path
from .views import blog_view, submit_view

urlpatterns = [
    path('', blog_view, name='blog'),
    path('submit/', submit_view, name='submit'),
]