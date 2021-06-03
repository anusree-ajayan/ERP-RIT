from django.db import models

# Create your models here.
class FacultyDetails(models.Model):
    fid = models.CharField(primary_key=True, max_length=50)
    name = models.TextField()
    deptname = models.CharField(max_length=100)
    phoneno = models.TextField()
    email = models.TextField()
    photo = models.ImageField()

    class Meta:
        managed = False
        db_table = 'faculty_details'


class Department(models.Model):
    deptname = models.CharField(primary_key=True, max_length=100)
    hod = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'


class ClassDetails(models.Model):
    classid = models.CharField(primary_key=True, max_length=50)
    courseid = models.CharField(max_length=50)
    semid = models.IntegerField()
    branch_or_specialisation = models.CharField(max_length=100)
    deptname = models.CharField(max_length=100)
    active = models.TextField()

    class Meta:
        managed = False
        db_table = 'class_details'


class StaffAdvisor(models.Model):
    classid = models.CharField(primary_key=True, max_length=50)
    fid = models.ForeignKey(FacultyDetails, models.DO_NOTHING,db_column='fid')
    students_list = models.TextField()

    class Meta:
        managed = False
        db_table = 'staff_advisor'


