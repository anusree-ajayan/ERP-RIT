from django.urls import path
from . import views

urlpatterns = [
      path('', views.Hod, name='Hod'),
      path('empreg.html',views.Hodhome, name='Hodhome'),

      path('viewstaff.html',views.view_faculty,name='view_faculty'), path('addfaculty',views.add_faculty, name='add_faculty'),
      path('staffreg.html',views.allot_staffadvisor,name='allot_staffadvisor'),
      path('viewstaffadvisor.html',views.view_staffadvisor,name='view_staffadvisor'),
      path('subreg.html', views.subreg, name='subreg'),
      path('subject_view.html', views.viewsubject, name='viewsubject'),
      path('suballoc.html', views.sub_allocate, name='sub_allocate'),
      path('suballoc_view.html', views.view_suballoc, name='view_suballoc'),
  ]