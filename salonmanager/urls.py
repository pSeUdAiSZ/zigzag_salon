from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


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
    path('update_appointment',views.update_appointment,name='update_appointment'),

    path('customer_list/', views.customer_list, name='customer_list'),
    path('customer_create/', views.customer_create, name='customer_create'),
    path('<int:pk>/', views.customer_detail, name='customer_detail'),
    path('<int:pk>/update/', views.customer_update, name='customer_update'),
    path('<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('search/', views.customer_search, name='customer_search'),

     path('branch/', views.branch_list, name='branch_list'),
    path('branch/create/', views.branch_create, name='branch_create'),
    path('branch/<int:pk>/', views.branch_detail, name='branch_detail'),
    path('branch/<int:pk>/update/', views.branch_update, name='branch_update'),
    path('branch/<int:pk>/delete/', views.branch_delete, name='branch_delete'),
     path('branch/search/', views.branch_search, name='branch_search'),

    path('staff-members/', views.staff_member_list, name='staff_member_list'),
    path('staff-members/create/', views.staff_member_create, name='staff_member_create'),
    path('staff-members/<int:pk>/', views.staff_member_detail, name='staff_member_detail'),
    path('staff-members/<int:pk>/update/', views.staff_member_update, name='staff_member_update'),
    path('staff-members/<int:pk>/delete/', views.staff_member_delete, name='staff_member_delete'),
    path('staff-members/search/', views.staff_member_search, name='staff_member_search'),
    #path('staff-members/search/', views.StaffMemberSearchView.as_view(), name='staff_member_search'),

    path('services/', views.service_list, name='service_list'),
    path('services/create/', views.service_create, name='service_create'),
    path('services/<int:pk>/', views.service_detail, name='service_detail'),
    path('services/<int:pk>/update/', views.service_update, name='service_update'),
    path('services/<int:pk>/delete/', views.service_delete, name='service_delete'),
    path('services/search/', views.service_search, name='service_search'),

    path('package/', views.package_list, name='package_list'),
    path('package/<int:package_id>/', views.package_detail, name='package_detail'),
    path('package/create/', views.package_create, name='package_create'),
    path('package/<int:package_id>/update/', views.package_update, name='package_update'),
    path('package/<int:package_id>/delete/', views.package_delete, name='package_delete'),
    path('packages/search/', views.package_search, name='package_search'),

    path('membership/purchase/', views.membership_purchase, name='membership_purchase'),
    path('membership/success/', views.membership_success, name='membership_success'),
    path('membership/family/add/', views.add_family_member, name='add_family_member'),
    
]
