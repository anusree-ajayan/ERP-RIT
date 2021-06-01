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

