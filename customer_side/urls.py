
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('customer_login', views.customer_login, name='customer_login'),
    path('customer_signup/', views.customer_signup, name='customer_signup'),
]