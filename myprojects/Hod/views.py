from django.shortcuts import render
from django.http import HttpResponse
from .models import FacultyDetails
from .models import Department
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
    details = FacultyDetails.objects.all()
    return render(request, 'viewstaff.html', {"FacultyDetails": details})
def allot_staffadvisor(request):
    return render(request,'allotstaffadvisor.html')
def view_staffadvisor(request):
    return render(request ,'viewstaffadvisor.html')
def subreg(request):
    return render(request,'subreg.html')
def viewsubject(request):
    return render(request,'subview.html')
def sub_allocate(request):
    return render(request,'suballoc.html')
def view_suballoc(request):
    return render(request,'suballocview.html')