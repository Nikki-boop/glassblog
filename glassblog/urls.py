from django.urls import path
from .views import blog_view, submit_view, update_post_view, delete_post_view
from .views_auth import login_view, logout_view, register_view

urlpatterns = [
    path('', blog_view, name='blog'),
    path('submit/', submit_view, name='submit'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('update/<int:post_id>/', update_post_view, name='update_post'),
    path('delete/<int:post_id>/', delete_post_view, name='delete_post'),
]