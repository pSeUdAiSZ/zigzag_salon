from django.shortcuts import render, redirect

def home(request):
    return render(request, 'salon_master/index.html')



def about_zigzag(request):
    return render(request, 'salon_master/about_zigzag.html')

def become_member(request):
    return render(request, 'salon_master/become_member.html')

def login_page(request):
    # Handle the login logic here
    return render(request, 'salon_master/login.html')





def about_view(request):
    return render(request, 'salon_master/about.html')

def services_view(request):
    return render(request, 'salon_master/services.html')

def portfolio_view(request):
    return render(request, 'salon_master/portfolio.html')

def blog_details_view(request):
    return render(request, 'salon_master/blog_details.html')

def contact_view(request):
    return render(request, 'salon_master/contact.html')

