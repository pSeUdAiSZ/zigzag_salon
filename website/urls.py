from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_view, name='about'),
    path('services/', views.services_view, name='services'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('blog_details/', views.blog_details_view, name='blog_details'),
    path('contact/', views.contact_view, name='contact'),

    path('about_zigzag/', views.about_zigzag, name='about_zigzag'),
    path('about/become_member/', views.become_member, name='become_member'),
    path('login/', views.login_page, name='login'),
]


