from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def login(request):
    return render(request,'login.html')
def login1(request):

    if request.method == 'POST':
        username = request.POST.get('nickname', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                request.session.set_expiry(86400)  # sets the exp. value of the session
                login(request, user)  # the user is now logged in
