from django.urls import path
from . import views
#
urlpatterns = [
    path('', views.login,name='log'),
    path('login1.html',views.login1,name='log1')

]