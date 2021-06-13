from django.urls import path
from . import views

urlpatterns = [
      path('', views.Hod, name='Hod'),
      path('empreg.html',views.Hodhome, name='Hodhome'),
      path('addfaculty', views.add_faculty, name='add_faculty'),
      path('viewstaff.html',views.view_faculty,name='view_faculty'),
      path('staffreg.html',views.allot_staffadvisor,name='allot_staffadvisor'),
      path('addstaff.html',views.add_staffadvisor,name='add_staffadvisor'),
      path('viewstaffadvisor.html',views.view_staffadvisor,name='view_staffadvisor'),
      path('subreg.html', views.subreg, name='subreg'),
      path('addsub.html', views.subadd, name='subadd'),
      path('subject_view.html', views.viewsubject, name='viewsubject'),
      path('suballoc.html', views.sub_allocate, name='sub_allocate'),
      path('addsuballoc.html',views.allocate_sub,name='suballocate_add'),
      path('suballocview.html', views.view_suballoc, name='view_suballoc'),
      path('searchstudent.html', views.searchstudent, name='searchstudent'),
      path('editstaff/<str:fid>', views.editstaff, name='editstaff'),
      path('deletestaff/<str:fid>',views.deletestaff,name= 'deletestaff'),
      path('editfac/<str:fid>',views.editfac,name= 'editfac'),
      path('deladfac/<str:fid>/<str:classid>',views.deletestaffadvisor,name='deletestaffadvisor'),
      path('editsub/<str:subjectid>',views.editsub,name='editsub'),
      path('editsub1/<str:subjectid>', views.editsub1, name='editsub1'),
      path('deletesub/<str:subjectid>',views.deletesub,name='deletesub'),
      path('editallo/<str:fid>/<str:subjectid>',views.editallotsub,name='editallotsub'),
      path('editsuballot/<str:classid>',views.editsuballot,name='editsuballot'),
  ]