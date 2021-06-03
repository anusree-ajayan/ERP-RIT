from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def login(request):
    return render(request,'login.html')
def login_redirect(request):

    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'],password=request.POST['password'])

        if user is not None:
            login(request,user)
            if user.login.usertype =='hod':
                return redirect('Hod:dash_home.html')
            else:
                messages.error(request,'username or password not correct')
                return redirect('login.html')
