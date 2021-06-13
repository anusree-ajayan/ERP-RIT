"""myprojects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', include('home.urls')),
    path('', include('Hod.urls')),
    path('empreg.html',include('Hod.urls')),
    path('addfaculty',include('Hod.urls')),
    path('viewstaff.html', include('Hod.urls')),
    path('staffreg.html', include('Hod.urls')),
    path('addsub.html',include('Hod.urls')),
    path('addstaff.html',include('Hod.urls')),
    path('viewstaffadvisor.html', include('Hod.urls')),
    path('subreg.html', include('Hod.urls')),
    path('subject_view.html', include('Hod.urls')),
    path('suballoc.html', include('Hod.urls')),
    path('addsuballoc.html',include('Hod.urls')),
    path('suballocview.html',include('Hod.urls')),
    path('searchstudent.html',include('Hod.urls')),
    path('editstaff/<str:fid>',include('Hod.urls')),
    path('deletestaff/<str:fid>',include('Hod.urls')),
    path('editfac/<str:fid>',include('Hod.urls')),
    path('deladfac/<str:fid>/<str:classid>',include('Hod.urls')),
    path('editsub/<str:subjectid>',include('Hod.urls')),
    path('editsub/<str:subjectid>',include('Hod.urls')),
    path('deletesub/<str:subjectid>',include('Hod.urls')),
    path('editallo/<str:fid>/<str:subjectid>',include('Hod.urls')),
    path('editsuballot/<str:classid>',include('Hod.urls')),
    path('delsubaloc/<str:subjectid>/<str:fid>/<str:classid>',include('Hod.urls')),
]
