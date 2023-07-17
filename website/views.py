from django.shortcuts import render

def home(request):
    return render(request, 'salon_master/index.html')
