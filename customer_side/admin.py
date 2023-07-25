from django.contrib import admin

from customer_side.models import Customer, Employee, User

# Register your models here.
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Employee)