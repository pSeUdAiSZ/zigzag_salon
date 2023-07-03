from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.manager_login, name='manager_login'),
    path('manager_signup/', views.manager_signup, name='manager_signup'),
    path('manager_dashboard/',views.manager_dashboard,name='manager_dashboard'),
    path('appointment_booking',views.appointment_booking,name='appointment_booking'),
    path('save_appointment', views.save_appointment, name='save_appointment'),
    path('service_create',views.service_create,name='service_create'),
    path('staff_member_create',views.staff_member_create,name='staff_member_create'),
    path('branch_create',views.branch_create,name='branch_create'),
    path('customer_create',views.customer_create,name='customer_create'),
    path('cancel_appointment',views.cancel_appointment,name='cancel_appointment'),
    path('confirm_appointment',views.confirm_appointment,name = 'confirm_appointment'),
    path('complete_appointment',views.complete_appointment,name='complete_appointment'),
    path('payment_options',views.payment_options,name=  'payment_options'),
    path('payment_options/<int:id>/<int:discount>',views.payment_options,name='payment_options'),
    path('payment_options/<int:id>',views.payment_options,name = 'payment_options'),
    path('edit_appointment',views.edit_appointment,name='edit_appointment'),
    path('move_appointment',views.move_appointment,name='move_appointment'),
    path('change_date_branch',views.change_date_branch,name='change_date_branch'),
    path('update_appointment',views.update_appointment,name='update_appointment'),
    path('add_discount/<int:id>/',views.add_discount,name='add_discount'),
    path('add_tips/<int:id>/', views.add_tips,name='add_tips')
]
