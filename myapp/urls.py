from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    #path('', views.LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('add/', views.add, name='add'),
    path('ref/', views.ref, name='ref'),
    #path('test', views.user, name='customer_form'),
]