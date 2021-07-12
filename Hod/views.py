from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import FacultyDetails
from .models import Department
from .models import ClassDetails
from .models import StaffAdvisor
from .models import SubjectClass, SubjectAllocation, StudDetails,FacultyDesignation
from django.contrib import messages


# Create your views here.
def Hod(request):
    userid=request.session["username"]
    name1=FacultyDetails.objects.get(fid=userid)
    print(name1.name)
    context = {
        'name1': name1,
    }
    return render(request, 'dash_home.html',context)


def Hodhome(request):
    results = Department.objects.all()
    return render(request, 'empreg.html', {"Department": results})


def add_faculty(request):
    if request.method == 'POST':
        fid = request.POST["fid"]
        name = request.POST["name"]
        deptname = request.POST["deptname"]
        phoneno = request.POST["phoneno"]
        email = request.POST["email"]
        fil_name = request.FILES["photo"]
        facob=FacultyDetails.objects.filter(fid=fid)
        if(facob.count()>0):

            messages.success(request, 'Staff is already registered!')
            return render(request, 'empreg.html')
        else:
            FacultyDetails(fid=fid, name=name, deptname=deptname, phoneno=phoneno, email=email, photo=fil_name).save()
            messages.success(request, 'Record Saved Successfully...!')
            fiid = FacultyDetails.objects.get(fid=fid)
            FacultyDesignation(fid=fiid, designation='Faculty').save()
            return render(request, 'empreg.html')

    else:

        return render(request, 'dash_home.html')


def view_faculty(request):
        details1 = Department.objects.all()
        userid = request.session["username"]
        name1 = FacultyDetails.objects.get(fid=userid)
        details2 = FacultyDetails.objects.raw('SELECT * FROM faculty_details WHERE deptname="'+name1.deptname+'"')
        return render(request, 'viewstaff.html', {"FacultyDetails": details2, "Department": details1})


def allot_staffadvisor(request):
    results1 = Department.objects.all()
    userid = request.session["username"]
    name1 = FacultyDetails.objects.get(fid=userid)
    results2 = FacultyDetails.objects.raw('SELECT * FROM faculty_details WHERE deptname="'+name1.deptname+'"')
    results3 = ClassDetails.objects.raw('SELECT * FROM class_details WHERE deptname="'+name1.deptname+'" and active like "yes"')

    return render(request, 'allotstaffadvisor.html',
                  {"Department": results1, "ClassDetails": results3, "FacultyDetails": results2})


def add_staffadvisor(request):
    if request.method == 'POST':
        classid = request.POST.get('class')
        fid = request.POST.get('fid')
        students_list = request.POST.get('list')
        fid_obj = FacultyDetails.objects.get(fid=fid)
        stfobj =StaffAdvisor.objects.filter(classid=classid,fid=fid,students_list=students_list).count()
        if(stfobj>0):
            messages.success(request, 'Staff Advisor Already Alloted to this Class!')
            return render(request, 'allotstaffadvisor.html')
        else:

            staff_ad = StaffAdvisor(fid=fid_obj, classid=classid, students_list=students_list)
            staff_ad.save()
            FacultyDesignation(fid=fid_obj,designation="Staff Advisor").save()

            messages.success(request, 'Record Saved Successfully...!')
            return render(request, 'allotstaffadvisor.html')
    else:
         return render(request,'allotstaffadvisor.html')

def view_staffadvisor(request):
        userid = request.session["username"]
        name1 = FacultyDetails.objects.get(fid=userid)

        vs1 = StaffAdvisor.objects.raw(
            'SELECT * FROM staff_advisor WHERE fid IN(SELECT fid FROM faculty_details WHERE deptname= "'+name1.deptname+'")')
        vs2 = Department.objects.all()
        print(vs1)
        return render(request, 'viewstaffadvisor.html', {"StaffAdvisor": vs1, "Department": vs2})



def subreg(request):
    userid = request.session["username"]
    name1 = FacultyDetails.objects.get(fid=userid)
    sub1 = ClassDetails.objects.raw('SELECT * FROM class_details WHERE  deptname="'+name1.deptname+'" and active like "yes"')
    res12=Department.objects.all()
    return render(request, 'subreg.html', {"ClassDetails":sub1,"Department":res12})
def loadclassid(request):
    deptname1=request.GET.get('deptname1')
    clssid=ClassDetails.objects.filter(deptname=deptname1)
    print(clssid)
    return render(request,'classid_dropdown.html',{"ClassDetails":clssid})



def subadd(request):
    if request.method == 'POST':
        subid = request.POST["subid"]
        name = request.POST["name"]
        classid = request.POST["deptname"]
        type = request.POST["type"]
        inpass = request.POST["inpass"]
        inmax = request.POST["inmax"]
        expass = request.POST["expass"]
        exmax = request.POST["exmax"]
        subad=SubjectClass.objects.filter(subjectid=subid,classid=classid).count()
        if(subad>0):
            messages.success(request, 'Subject Already Exists...!')
            return render(request, 'subreg.html')
        else:
             sub_ad = SubjectClass(subjectid=subid, subject_title=name, classid=classid, type=type, internal_passmark=inpass,
                              internal_mark=inmax, external_pass_mark=expass, external_mark=exmax)
             sub_ad.save()
             messages.success(request, 'Record Saved Successfully...!')
             return render(request, 'subreg.html')
    else:

        return render(request, 'subreg.html')


def viewsubject(request):
        userid = request.session["username"]
        name1 = FacultyDetails.objects.get(fid=userid)
        res1 = Department.objects.all()
        vwsub = SubjectClass.objects.raw('SELECT * FROM subject_class WHERE classid IN(SELECT classid FROM class_details WHERE deptname= "'+name1.deptname+'")')
        return render(request, 'subview.html', {"SubjectClass": vwsub, "Department": res1})



def sub_allocate(request):
    userid = request.session["username"]
    name1 = FacultyDetails.objects.get(fid=userid)
    subaloc = ClassDetails.objects.raw('SELECT * FROM class_details WHERE deptname="' + name1.deptname + '" and active like "yes"')
    subname = SubjectClass.objects.raw('SELECT * FROM subject_class WHERE classid IN(SELECT classid FROM class_details WHERE deptname="' + name1.deptname + '" and active like "yes")')
    fname1 = FacultyDetails.objects.raw('SELECT * FROM faculty_details WHERE deptname="' + name1.deptname + '"')
    rest1 = Department.objects.all()
    return render(request, 'suballoc.html', {"ClassDetails":subaloc, "SubjectClass":subname, "FacultyDetails":fname1, "Department":rest1})


def allocate_sub(request):
    if request.method == 'POST':
        classid = request.POST.get('classid')
        subjectid = request.POST.get('subjectid')
        fid1 = request.POST.get('fid')
        type = request.POST.get('type')
        fid_obj1 = FacultyDetails.objects.get(fid=fid1)
        fid_obj2 = SubjectClass.objects.filter(subjectid=subjectid,classid=classid)[0]
        fid_obj3 = SubjectClass.objects.filter(classid=classid,subjectid=subjectid)[0]
        subalo =SubjectAllocation.objects.filter(fid=fid1,subjectid=subjectid,classid=classid).count()
        if(subalo>0):
            messages.success(request, 'Already allotted as Main or Sub Faculty...!')
            return render(request, 'suballoc.html')
        else:

           alloc_d= SubjectAllocation(classid=fid_obj3,subjectid=fid_obj2,fid=fid_obj1,type=type)
           alloc_d.save()
           messages.success(request, 'Record Saved Successfully...!')
           return render(request, 'suballoc.html')
    else:
        return render(request, 'suballoc.html')


def view_suballoc(request):
        userid = request.session["username"]
        name1 = FacultyDetails.objects.get(fid=userid)
        classid1 = request.POST.get('classid')
        deptm = Department.objects.all()
        subaloc21 = ClassDetails.objects.raw('SELECT  classid FROM class_details WHERE deptname="' + name1.deptname + '" and active like "YES" ')

        subalocview = SubjectAllocation.objects.all()

        return render(request, 'suballocview.html',
                      { "Department": deptm, "SubjectAllocation": subalocview})



def searchstudent(request):
    if request.method == 'POST':
        adno = request.POST.get('adno')
        resu = StudDetails.objects.filter(admissionno=adno)
        return render(request, 'searchstudent.html', {"StudDetails": resu})
    else:
        return render(request, 'searchstudent.html')

def editstaff(request,fid):
    var = FacultyDetails.objects.get(fid=fid)
    context = {
        'var': var,
    }
    return render(request,'editfaculty.html', context)
def editfac(request,fid):
    if request.method == 'POST':
        fid=request.POST["fid"]
        name = request.POST["name"]
        deptname = request.POST["deptname"]
        phoneno = request.POST["phoneno"]
        email = request.POST["email"]
        fil_name = request.POST["photo"]
        facob=FacultyDetails.objects.get(fid=fid)
        faculty_d = FacultyDetails(fid=fid, name=name, deptname=deptname, phoneno=phoneno, email=email, photo=fil_name)
        faculty_d.save()
        messages.success(request, 'Record Updated Successfully...!')
        return render(request, 'editfaculty.html')
    else:
        return render(request, 'editfaculty.html')
def deletestaff(request,fid):
    var1 = FacultyDetails.objects.get(fid=fid)
    var1.delete()
    var21=FacultyDesignation.objects.filter(fid=fid,designation='Faculty')
    var21.delete()
    messages.success(request, 'Record Is Deleted..!')
    return render(request,'viewstaff.html')
def deletestaffadvisor(request,fid,classid):
    var2=StaffAdvisor.objects.get(fid=fid,classid=classid)
    var2.delete()
    var211 = FacultyDesignation.objects.filter(fid=fid,designation='Staff Advisor')
    var211.delete()
    messages.success(request, 'Record Is Deleted..!')
    return render(request,'viewstaffadvisor.html')
def editsub(request,subjectid):
    varsub = SubjectClass.objects.get(subjectid=subjectid)
    context = {
        'varsub': varsub,
    }
    return render(request, 'editsub.html', context)
def editsub1(request,subjectid):
    if request.method == 'POST':
        subid = request.POST["subid"]
        name = request.POST["name"]
        classid = request.POST["deptname"]
        type = request.POST["type"]
        inpass = request.POST["inpass"]
        inmax = request.POST["inmax"]
        expass = request.POST["expass"]
        exmax = request.POST["exmax"]
        subjectid=SubjectClass.objects.get(subjectid=subjectid)
        sub_ad = SubjectClass(subjectid=subid, subject_title=name, classid=classid, type=type, internal_passmark=inpass,
                              internal_mark=inmax, external_pass_mark=expass, external_mark=exmax)
        sub_ad.save()
        messages.success(request, 'Record Updated Successfully...!')
        return render(request, 'editsub.html')
    else:
        return render(request, 'editsub.html')

def deletesub(request,subjectid):
    varsub = SubjectClass.objects.get(subjectid=subjectid)
    varsub.delete()
    messages.success(request, 'Record Is Deleted..!')
    return render(request,'subview.html')
def editallotsub(request,fid,subjectid):
    varsubaloc=SubjectAllocation.objects.get(fid=fid,subjectid=subjectid)
    context = {
        'varsubaloc': varsubaloc,
    }

    return render(request,'editsuballoc.html',context)
def editsuballot(request,classid):
    if request.method == 'POST':
        classid1 = request.POST.get(classid)
        subjectid = request.POST.get('subjectid')
        fid1 = request.POST.get('fid')
        type = request.POST.get('type')
        objfid=FacultyDetails.objects.get(fid=fid1)
        objsub=SubjectClass.objects.filter(subjectid=subjectid)[0]
        objclass=SubjectClass.objects.filter(classid=classid).first()
        alloc_d = SubjectAllocation(classid=objclass, subjectid=objsub, fid=objfid, type=type)
        alloc_d.save()
        messages.success(request, 'Record Updated Successfully...!')
        return render(request, 'editsuballoc.html')
    else:
        return render(request, 'editsuballoc.html')

def delsubalot(request,subjectid,fid,classid):
    subalott=SubjectAllocation.objects.get(subjectid=subjectid,fid=fid,classid=classid)
    subalott.delete()
    messages.success(request, 'Record Is Deleted..!')
    return render(request ,'suballocview.html')