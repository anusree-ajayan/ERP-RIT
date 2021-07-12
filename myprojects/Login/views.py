from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Login

# Create your views here.

def login(request):

    return render(request,'login.html')
def login1(request):
   if request.method=='POST':
        username= request.POST["username"]
        password= request.POST["password"]
        log = Login.objects.filter(username=username,password=password)
        log1= Login.objects.get(username=username,password=password)

        if(log1.usertype=='hod'):
           request.session["username"]=username
           return redirect("/Hod/")
        else:
            return render(request, 'login.html')


   return render(request, 'login.html')