from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name='users'),
    path('user/<int:pk>/edit/', views.user_edit, name='user_edit'),
    path('registration/', views.user_new, name='user_new'),
]