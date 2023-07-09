from datetime import date, timedelta
from decimal import Decimal
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import StaffMember,Customer,Service,Branch,Appointment

from .utils import timeslot_gen_tf,calculate_end_time

# Create your views here.
def manager_signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('manager_login')
    return render (request,'manager_signup.html')

def manager_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            
            return redirect('manager_dashboard')
        else:
            return redirect('manager_login')
    return render (request,'manager_login.html')
@login_required(login_url='/salonmanager/login/')
def manager_dashboard(request):
    return render(request,'base.html')

def appointment_booking(request):

    """if request.method == 'POST':
        selected_customer = request.POST.get('customer')
        customer = get_object_or_404(Customer, id=selected_customer)
    """
    time_slot_tf = timeslot_gen_tf('10:00 AM','10:00 PM')
    appointment_list=[]
    staff_members_list= StaffMember.objects.all()
    today_date = date.today()
    
    branches  = Branch.objects.all()
    if request.method =='POST':
        selected_date = request.POST.get('selected_date')
        selected_time = request.POST.get('selected_time')
        selected_staff = request.POST.get('selected_staff')
        selected_branch = request.POST.get('selected_branch')
        selected_services = request.POST.getlist('service-name')
        selected_customer = request.POST.get('customer')
        customer = get_object_or_404(Customer,id=  selected_customer)
        staff = get_object_or_404(StaffMember, name= selected_staff)
        branch = get_object_or_404(Branch,name = selected_branch)
        
        total_duration = timedelta()
        total_prices=[]
        services_list = []
        for services in selected_services:
            service_objs = Service.objects.get(name = services)
            duration = service_objs.duration
            total_prices.append(service_objs.price)
            total_duration = total_duration+duration
            services_list.append(service_objs)
            
        end_time = calculate_end_time(selected_time,total_duration)
        total_price = sum([Decimal(str(price.amount)) for price in total_prices])
        print(selected_time,end_time,total_price)
        appointment_details= Appointment.objects.create(
             customer=customer,
            staff_member=staff,
            start_time=selected_time,
            end_time=end_time,
            date=selected_date,
            total_price = total_price,
            status = 'booked',
            branch = branch,
        )
        appointment_details.services.set(services_list)
    
        
    if Appointment.objects.exists:
        today = date.today()
        appointment_list_today = Appointment.objects.filter(date=today)
    for appointment in appointment_list_today:
        customer_id = appointment.customer_id
        customer  = get_object_or_404(Customer,id = customer_id)
        staff_member_id = appointment.staff_member_id
        staff_member = get_object_or_404(StaffMember,id = staff_member_id)
        branch_id = appointment.branch_id
        branch = get_object_or_404(Branch,id=branch_id)
        start_time_str = appointment.start_time.strftime("%H:%M:%S")
        services = appointment.services.all()
        duration=timedelta()
        service_names = []
        for service in services:
            duration += service.duration
            service_names.append(service.name)
                
        duration_minutes = duration.total_seconds() // 60  # Calculate duration in minutes
        height = duration_minutes * 33 / 15
        print(height)
        appointment_dict={
                'customer':customer,
                'staff_member':staff_member.name,
                'start_time':start_time_str,
                'end_time':appointment.end_time,
                'date':appointment.date,
                'total_price':appointment.total_price,
                'status':appointment.status,
                'branch':branch,
                'services': service_names,
                'id':appointment.pk,
                'height':height
            }
        print(appointment_dict['id'])
        print(type(appointment_dict['start_time']))
        appointment_list.append(appointment_dict)
    print(appointment_list)
    print(today)
    context={'time_slots':time_slot_tf,'staff_members':staff_members_list,'branches':branches,'appointment_details_list':appointment_list,'date_chosen':today_date}
    return render(request,'appointment_booking.html',context)
def save_appointment(request):
    existing_customer=  Customer.objects.all
    staff_members = StaffMember.objects.all
    services = Service.objects.all
    categories = Service.objects.values_list('category', flat=True).distinct()
    branches = Branch.objects.all()
    
    
    global selected_date, selected_time, selected_staff,selected_branch
    if request.method == 'POST':
        selected_staff = request.POST.get('staff-name')
        selected_time = request.POST.get('start-time')
        selected_date = request.POST.get('date')
        selected_branch = request.POST.get('branch')
    
    
    context={
        'existing_customers':existing_customer,'selected_staff':selected_staff,'selected_time':selected_time,'selected_date':selected_date,
        'selected_branch': selected_branch,'services':services,'categories':categories,'staff_members':staff_members,'branches':branches    }
        
    return render(request, 'save_appointment.html',context)
def cancel_appointment(request):
    if request.method == 'POST':
        appointment_id =request.POST.get('appointment_id')
        print(appointment_id)
        appointment = Appointment.objects.get(id=appointment_id)
        print('cancelled', appointment)
        appointment.status = 'cancelled'
        appointment.save()
    return redirect('appointment_booking')

def complete_appointment(request):
    if request.method == 'POST':
        appointment_id =request.POST.get('appointment_id')
        print(appointment_id)
        appointment = Appointment.objects.get(id=appointment_id)
        
        appointment.status = 'completed'
        appointment.save()
    return redirect('appointment_booking')

def confirm_appointment(request):
    if request.method == 'POST':
        appointment_id =request.POST.get('appointment_id')
        print(appointment_id)
        appointment = Appointment.objects.get(id=appointment_id)
        
        appointment.status = 'confirmed'
        appointment.save()
    return redirect('appointment_booking')

def payment_options(request):
    return redirect('appointment_booking')
def edit_appointment(request):
    return redirect('save_appointment')
def move_appointment(request):
    if request.method =='POST':
        appointment_id = request.POST.get('appointment_id')
    appointment =  get_object_or_404(Appointment, id = appointment_id)
    appointment_dict = {
        'customer':appointment.customer,
        'staff_member':appointment.staff_member,
        'start-time':appointment.start_time,
        'date':appointment.date,
        'branch':appointment.branch,
        'id':appointment.id
    }
    staff_member_list = StaffMember.objects.filter(branches = appointment.branch )
    time_slot = timeslot_gen_tf('10:00 AM','10:00 PM')
    context={
        'appointment_dict':appointment_dict,
        'staff_member_list':staff_member_list,
        'time_slots':time_slot
    }
    return render(request,'move_appointment.html',context)
def update_appointment(request):
    if request.method =='POST':
        appointment_id = request.POST.get('appointment_id')
        new_staff_id = request.POST.get('new_staff')
        new_staff = get_object_or_404(StaffMember,id= new_staff_id)
        new_start_time = request.POST.get('new_start')
        new_date = request.POST.get('new_date')
        appointment = get_object_or_404(Appointment,id = appointment_id)
        appointment.staff_member = new_staff
        appointment.start_time = new_start_time
        appointment.date = new_date
        appointment.save()
    print(appointment)
    return redirect('appointment_booking')
        

def change_date_branch(request):
    appointment_list=[]
    branches = Branch.objects.all()
    time_slot_tf = timeslot_gen_tf('10:00 AM','10:00 PM')
    if request.method =='POST':
        date_chosen = request.POST.get('date_chosen')
        branch_chosen = request.POST.get('branch_chosen')
        chosen_branch = get_object_or_404(Branch,id= branch_chosen)
    staff_members_list = StaffMember.objects.filter(branches = branch_chosen)
    appointment_list_selected = Appointment.objects.filter(date=date_chosen,branch = branch_chosen)
    print(appointment_list_selected)
    for appointment in appointment_list_selected:
        customer_id = appointment.customer_id
        customer  = get_object_or_404(Customer,id = customer_id)
        staff_member_id = appointment.staff_member_id
        staff_member = get_object_or_404(StaffMember,id = staff_member_id)
        branch_id = appointment.branch_id
        branch = get_object_or_404(Branch,id=branch_id)
        start_time_str = appointment.start_time.strftime("%H:%M:%S")
        services = appointment.services.all()
        duration=timedelta()
        service_names = []
        for service in services:
            duration += service.duration
            service_names.append(service.name)
                
        duration_minutes = duration.total_seconds() // 60  # Calculate duration in minutes
        height = duration_minutes * 33 / 15
        print(height)
        appointment_dict={
                'customer':customer,
                'staff_member':staff_member.name,
                'start_time':start_time_str,
                'end_time':appointment.end_time,
                'date':appointment.date,
                'total_price':appointment.total_price,
                'status':appointment.status,
                'branch':branch,
                'services': service_names,
                'id':appointment.pk,
                'height':height
            }
        appointment_list.append(appointment_dict)
    context = {'time_slots':time_slot_tf,'staff_members':staff_members_list,'branches':branches,'appointment_details_list':appointment_list,'date_chosen':date_chosen,
               'branch_chosen':chosen_branch}
    return render(request,'appointment_booking.html',context)


from django.shortcuts import render, redirect
from .models import Customer

from django.shortcuts import render, redirect
from .models import Customer

"""def add_customer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        profession = request.POST.get('profession')
        address = request.POST.get('address')
        customer = Customer(name=name, email=email, phone_number=phone_number, profession=profession, address=address)
        customer.save()
        return redirect('save_appointment')

    return render(request, 'customer_create.html')
"""


from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import CustomerForm
from django.contrib import messages

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'customer_details.html', {'customer': customer})

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customer_create.html', {'form': form})

def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_detail', pk=customer.pk)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer_update.html', {'form': form, 'customer': customer})

def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'customer_delete.html', {'customer': customer})

def customer_search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            customers = Customer.objects.filter(name__icontains=query)
        else:
            customers = Customer.objects.all()
        return render(request, 'customer_list.html', {'customers': customers})




from .models import Branch
from .forms import BranchForm

def branch_list(request):
    branches = Branch.objects.all()
    return render(request, 'branch_list.html', {'branches': branches})

def branch_detail(request, pk):
    branch = Branch.objects.get(pk=pk)
    return render(request, 'branch_details.html', {'branch': branch})

def branch_create(request):
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('branch_list')
    else:
        form = BranchForm()
    return render(request, 'branch_create.html', {'form': form})

def branch_update(request, pk):
    branch = Branch.objects.get(pk=pk)
    if request.method == 'POST':
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            form.save()
            return redirect('branch_detail',pk=branch.pk)
    else:
        form = BranchForm(instance=branch)
    return render(request, 'branch_update.html', {'form': form, 'branch': branch})

def branch_delete(request, pk):
    branch = Branch.objects.get(pk=pk)
    if request.method == 'POST':
        branch.delete()
        return redirect('branch_list')
    return render(request, 'branch_delete.html', {'branch': branch})

from django.shortcuts import render
from .models import Branch

def branch_search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            branches = Branch.objects.filter(name__icontains=query)
        else:
            branches = Branch.objects.all()
        return render(request, 'branch_list.html', {'branches': branches})





from .models import StaffMember
from .forms import StaffMemberForm

# StaffMember list
def staff_member_list(request):
    staff_members = StaffMember.objects.all()
    return render(request, 'staff_member_list.html', {'staff_members': staff_members})

# StaffMember detail
def staff_member_detail(request, pk):
    staff_member = get_object_or_404(StaffMember, pk=pk)
    return render(request, 'staff_member_detail.html', {'staff_member': staff_member})


# StaffMember create
from .models import Branch, StaffMember
from .forms import StaffMemberForm

def staff_member_create(request):
    branches = Branch.objects.all()

    if request.method == 'POST':
        form = StaffMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_member_list')
    else:
        form = StaffMemberForm()

    context = {
        'form': form,
        'branches': branches
    }
    return render(request, 'staff_member_create.html', context)


# StaffMember update
def staff_member_update(request, pk):
    staff_member = get_object_or_404(StaffMember, pk=pk)
    if request.method == 'POST':
        form = StaffMemberForm(request.POST, request.FILES, instance=staff_member)
        if form.is_valid():
            form.save()
            return redirect('staff_member_list')
    else:
        form = StaffMemberForm(instance=staff_member)
    return render(request, 'staff_member_update.html', {'form': form, 'staff_member': staff_member})

# StaffMember delete
def staff_member_delete(request, pk):
    staff_member = get_object_or_404(StaffMember, pk=pk)
    if request.method == 'POST':
        staff_member.delete()
        return redirect('staff_member_list')
    return render(request, 'staff_member_delete.html', {'staff_member': staff_member})


from django.db.models import Q

def staff_member_search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            staff_members = StaffMember.objects.filter(name__icontains=query)
        else:
            staff_members = StaffMember.objects.all()
        return render(request, 'staff_member_list.html', {'staff_members': staff_members})



from .models import Service
from .forms import ServiceForm

def service_list(request):
    services = Service.objects.all()
    return render(request, 'service_list.html', {'services': services})

def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'service_create.html', {'form': form})

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'service_detail.html', {'service': service})

def service_update(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_detail', pk=service.pk)
    else:
        form = ServiceForm(instance=service)
    return render(request, 'service_update.html', {'form': form, 'service': service})

def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('service_list')
    return render(request, 'service_delete.html', {'service': service})


def service_search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            services = Service.objects.filter(name__icontains=query)
        else:
            services = Service.objects.all()
        return render(request, 'service_list.html', {'services': services})



from django.shortcuts import render, get_object_or_404, redirect
from .forms import PackageForm
from .models import Packages

def package_list(request):
    packages = Packages.objects.all()
    return render(request, 'package_list.html', {'packages': packages})

def package_detail(request, package_id):
    package = get_object_or_404(Packages, id=package_id)
    return render(request, 'package_detail.html', {'package': package})

def package_create(request):
    services = Service.objects.all()
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('package_list')
    else:
        form = PackageForm()
    context = {
        'form': form,
        'services': services
    }
    return render(request, 'package_create.html', {'form': form})

def package_update(request, package_id):
    package = get_object_or_404(Packages, pk=package_id)

    if request.method == 'POST':
        form = PackageForm(request.POST, instance=package)
        if form.is_valid():
            form.save()
            return redirect('package_detail', package_id=package_id)
    else:
        form = PackageForm(instance=package)

    context = {
        'form': form,
        'package': package,
    }
    return render(request, 'package_update.html', context)


def package_delete(request, package_id):
    package = get_object_or_404(Packages, id=package_id)
    if request.method == 'POST':
        package.delete()
        return redirect('package_list')
    return render(request, 'package_delete.html', {'package': package})


def package_search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            packages = Packages.objects.filter(name__icontains=query)
        else:
            packages = Packages.objects.all()
        return render(request, 'package_list.html', {'packages': packages})

