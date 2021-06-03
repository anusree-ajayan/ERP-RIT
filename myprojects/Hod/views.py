from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import FacultyDetails
from .models import Department
from .models import ClassDetails
from .models import StaffAdvisor
from django.contrib import messages
# Create your views here.
def Hod(request):
    return render(request, 'dash_home.html')
def Hodhome(request):
    results=Department.objects.all()
    return render(request, 'empreg.html',{"Department":results})

def add_faculty(request):

    if request.method == 'POST':
        fid = request.POST["fid"]
        name = request.POST["name"]
        deptname = request.POST["deptname"]
        phoneno = request.POST["phoneno"]
        email = request.POST["email"]
        fil_name = request.FILES["photo"]
        faculty_d = FacultyDetails(fid=fid,name=name,deptname=deptname,phoneno=phoneno,email=email,photo=fil_name)
        faculty_d.save()
        messages.success(request,'Record Saved Successfully...!')
        return render(request,'empreg.html')
    else:

         return render(request,'dash_home.html')


def view_faculty(request):
  if request.method == 'POST':
      dept = request.POST.get('deptna')
      details2= FacultyDetails.objects.raw('SELECT * FROM faculty_details WHERE deptname = "'+dept+'"')
      return render(request,'viewstaff.html',{"FacultyDetails": details2})
  else:

      details1 = FacultyDetails.objects.all()
      return render(request, 'viewstaff.html', {"FacultyDetails": details1})


def allot_staffadvisor(request):
    results1 = Department.objects.all()
    results2 = FacultyDetails.objects.all()
    results3 =ClassDetails.objects.all()

    return render(request,'allotstaffadvisor.html',{"Department":results1,"ClassDetails":results3,"FacultyDetails":results2})

def add_staffadvisor(request):
    if request.method == 'POST':
        classid = request.POST.get('class')
        fid = request.POST.get('fid')
        students_list = request.POST.get('list')
        fid_obj=FacultyDetails.objects.get(fid=fid)
        staff_ad= StaffAdvisor(fid=fid_obj,classid=classid,students_list=students_list)
        staff_ad.save()
        messages.success(request, 'Record Saved Successfully...!')

    return render(request, 'allotstaffadvisor.html')
def view_staffadvisor(request):
       vs1 = StaffAdvisor.objects.all()
       vs2 = ClassDetails.objects.all()
       return render(request,'viewstaffadvisor.html',{"StaffAdvisor": vs1,"ClassDetails":vs2})
def subreg(request):
    return render(request,'subreg.html')
def viewsubject(request):
    return render(request,'subview.html')
def sub_allocate(request):
    return render(request,'suballoc.html')
def view_suballoc(request):
    return render(request,'suballocview.html')