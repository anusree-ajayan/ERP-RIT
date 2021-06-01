from django.urls import path
from . import views
#
urlpatterns = [
    path('login/', views.login,name='log'),
    path('login1.html', views.login1, name='login1'),
]