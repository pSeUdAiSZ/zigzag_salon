
from imaplib import _Authenticator
from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def customer_signup(request):
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
            return redirect('customer_login')
    return render (request,'customer_signup.html')


@login_required(login_url='/customer_side/login/')

def customer_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            
            return redirect('manager_dashboard')
        else:
            return redirect('customer_login')
    return render (request,'customer_login.html')
