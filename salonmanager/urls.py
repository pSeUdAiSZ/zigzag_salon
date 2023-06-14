from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.manager_login, name='manager_login'),
    path('manager_signup/', views.manager_signup, name='manager_signup'),
    path('manager_dashboard/',views.manager_dashboard,name='manager_dashboard'),
    path('appointment_booking',views.appointment_booking,name='appointment_booking'),
    path('save_appointment', views.save_appointment, name='save_appointment'),
    path('cancel_appointment',views.cancel_appointment,name='cancel_appointment'),
    path('confirm_appointment',views.confirm_appointment,name = 'confirm_appointment'),
    path('complete_appointment',views.complete_appointment,name='complete_appointment'),
    path('payment_options',views.payment_options,name=  'payment_options'),
    path('edit_appointment',views.edit_appointment,name='edit_appointment'),
    path('move_appointment',views.move_appointment,name='move_appointment'),
    path('change_date_branch',views.change_date_branch,name='change_date_branch'),
    path('update_appointment',views.update_appointment,name='update_appointment')
]
