from django.urls import path
from . import views
#
urlpatterns = [
    path('log', views.login,name='log'),
    path('login1.html', views.login_redirect, name='login1'),
]