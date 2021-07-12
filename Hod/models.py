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
    fid = models.ForeignKey(FacultyDetails, models.DO_NOTHING, db_column='fid')
    students_list = models.TextField()

    class Meta:
        managed = False
        db_table = 'staff_advisor'


class SubjectClass(models.Model):
    subjectid = models.CharField(primary_key=True, max_length=50)
    subject_title = models.TextField()
    classid = models.CharField(max_length=50)
    type = models.CharField(max_length=30)
    internal_passmark = models.IntegerField()
    internal_mark = models.IntegerField()
    external_pass_mark = models.IntegerField()
    external_mark = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'subject_class'
        unique_together = (('subjectid', 'classid'),)


class SubjectAllocation(models.Model):
    classid = models.OneToOneField("SubjectClass", models.DO_NOTHING, db_column='classid', primary_key=True)
    subjectid = models.ForeignKey("SubjectClass", models.DO_NOTHING, db_column='subjectid',  related_name='subid+')
    fid = models.ForeignKey(FacultyDetails, models.DO_NOTHING, db_column='fid')
    type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'subject_allocation'
        unique_together = (('classid', 'subjectid', 'fid', 'type'),)


class StudDetails(models.Model):
    admissionno = models.CharField(primary_key=True, max_length=50)
    name = models.TextField(blank=True, null=True)
    dob = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    religion = models.TextField(blank=True, null=True)
    caste = models.TextField(blank=True, null=True)
    year_of_admission = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    mobile_phno = models.TextField(blank=True, null=True)
    land_phno = models.TextField()
    address = models.TextField(blank=True, null=True)
    rollno = models.TextField(blank=True, null=True)
    rank = models.TextField(blank=True, null=True)
    quota = models.TextField(blank=True, null=True)
    school_1 = models.TextField(blank=True, null=True)
    regno_1 = models.TextField(blank=True, null=True)
    board_1 = models.TextField(blank=True, null=True)
    percentage_1 = models.TextField()
    school_2 = models.TextField(blank=True, null=True)
    regno_2 = models.TextField(blank=True, null=True)
    board_2 = models.TextField(blank=True, null=True)
    percentage_2 = models.TextField()
    no_chance1 = models.TextField(blank=True, null=True)
    name_last_studied = models.TextField()
    courseid = models.TextField(blank=True, null=True)
    branch_or_specialisation = models.TextField(blank=True, null=True)
    branch_code = models.CharField(max_length=20)
    image = models.TextField()
    gate_score = models.IntegerField()
    admission_type = models.CharField(max_length=30)
    entry_sem = models.IntegerField()
    exit_sem = models.IntegerField()
    status = models.CharField(max_length=50)
    blood = models.CharField(max_length=5)
    image_status = models.CharField(max_length=50, blank=True, null=True)
    tc_no_adm = models.CharField(max_length=100, blank=True, null=True)
    tc_date_adm = models.DateField(blank=True, null=True)
    date_of_admission = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stud_details'
class FacultyDesignation(models.Model):
    fid = models.ForeignKey('FacultyDetails', models.DO_NOTHING, db_column='fid')
    designation = models.TextField()

    class Meta:
        managed = False
        db_table = 'faculty_designation'