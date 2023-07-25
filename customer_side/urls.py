
from os import path
from django import views


urlpatterns = [
    path('', views.customer_login, name='customer_login'),
    path('customer_signup/', views.customer_signup, name='customer_signup'),
]