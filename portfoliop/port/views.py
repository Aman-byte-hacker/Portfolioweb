from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,"index.html")
   

def skills(request):
    return render(request,"skills.html")

def certi(request):
    return render(request,"certi.html")    

def projects(request):
    return render(request,"projects.html")    

def contact(request):
    if request.method == "POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        subject=request.POST.get('subject')
        data=Contact(firstname=firstname,lastname=lastname,subject=subject)
        data.save()
        messages.success(request, "Your Message Has Been sent!")
    return render(request,"contact.html")    