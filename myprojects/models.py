# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AcademicYear(models.Model):
    year_id = models.AutoField(primary_key=True)
    acd_year = models.TextField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'academic_year'


class AdmissionStatus(models.Model):
    id = models.IntegerField(blank=True, null=True)
    course = models.CharField(max_length=2, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admission_status'


class Attendance(models.Model):
    attid = models.AutoField(primary_key=True)
    date = models.DateField()
    hour = models.IntegerField()
    subjectid = models.ForeignKey('SubjectClass', models.DO_NOTHING, db_column='subjectid')
    classid = models.ForeignKey('SubjectClass', models.DO_NOTHING, db_column='classid')
    studid = models.ForeignKey('StudDetails', models.DO_NOTHING, db_column='studid')
    status = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'attendance'


class Attendanceold(models.Model):
    attid = models.IntegerField(primary_key=True)
    date = models.DateField()
    hour = models.IntegerField()
    subjectid = models.CharField(max_length=50)
    classid = models.CharField(max_length=50)
    studid = models.CharField(max_length=50)
    status = models.CharField(max_length=1)
    acd_year = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendanceold'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Cc(models.Model):
    cc_no = models.AutoField(primary_key=True)
    adm_no = models.CharField(max_length=50)
    chrctr = models.TextField()

    class Meta:
        managed = False
        db_table = 'cc'


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


class Complaint(models.Model):
    id_com = models.AutoField(primary_key=True)
    stud_id = models.CharField(max_length=20)
    fid = models.CharField(max_length=20)
    com_type = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    content = models.CharField(max_length=250)
    com_time = models.DateTimeField()
    response = models.CharField(max_length=300, blank=True, null=True)
    res_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    designation = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complaint'


class CourseAcademic(models.Model):
    course_id = models.CharField(max_length=100)
    year_id = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'course_academic'


class Courses(models.Model):
    id = models.CharField(primary_key=True, max_length=5)
    course = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    no_of_semesters = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'courses'


class CurrentClass(models.Model):
    classid = models.CharField(max_length=50)
    studid = models.OneToOneField('StudDetails', models.DO_NOTHING, db_column='studid', primary_key=True)
    rollno = models.IntegerField()
    adm_status = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'current_class'


class CurrentClassSemreg(models.Model):
    classid = models.CharField(max_length=50)
    studid = models.CharField(primary_key=True, max_length=50)
    rollno = models.IntegerField()
    adm_status = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'current_class_semreg'


class CurrentClassold(models.Model):
    classid = models.CharField(max_length=50)
    studid = models.CharField(max_length=50)
    rollno = models.IntegerField()
    year = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'current_classold'


class Department(models.Model):
    deptname = models.CharField(primary_key=True, max_length=100)
    hod = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DutyLeave(models.Model):
    studid = models.ForeignKey('StudDetails', models.DO_NOTHING, db_column='studid')
    subjectid = models.ForeignKey('SubjectClass', models.DO_NOTHING, db_column='subjectid')
    leave_date = models.DateField()
    hour = models.IntegerField()
    remark = models.TextField(blank=True, null=True)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'duty_leave'


class DutyLeaveold(models.Model):
    id = models.IntegerField()
    studid = models.CharField(max_length=100)
    subjectid = models.CharField(max_length=100)
    leave_date = models.DateField()
    hour = models.IntegerField()
    remark = models.TextField()
    date = models.DateTimeField()
    acd_year = models.TextField()
    classid = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'duty_leaveold'


class EachSessionalMarks(models.Model):
    series_no = models.IntegerField(primary_key=True)
    classid = models.ForeignKey(ClassDetails, models.DO_NOTHING, db_column='classid')
    studid = models.ForeignKey('StudDetails', models.DO_NOTHING, db_column='studid')
    subjectid = models.ForeignKey('SubjectClass', models.DO_NOTHING, db_column='subjectid')
    sessional_marks = models.FloatField()
    sessional_remark = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    sessional_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'each_sessional_marks'
        unique_together = (('series_no', 'classid', 'studid', 'subjectid'),)


class EachSessionalMarksold(models.Model):
    series_no = models.IntegerField()
    classid = models.CharField(max_length=50)
    studid = models.CharField(max_length=50)
    subjectid = models.CharField(max_length=50)
    sessional_marks = models.FloatField()
    sessional_remark = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    sessional_date = models.DateTimeField()
    acd_year = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'each_sessional_marksold'


class ElectiveStudent(models.Model):
    sub_code = models.ForeignKey('SubjectClass', models.DO_NOTHING, db_column='sub_code')
    stud = models.ForeignKey('StudDetails', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'elective_student'


class ElectiveStudentold(models.Model):
    sub_code = models.CharField(max_length=50)
    stud_id = models.CharField(max_length=50)
    acd_year = models.TextField()
    classid = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'elective_studentold'


class FacultyDesignation(models.Model):
    fid = models.ForeignKey('FacultyDetails', models.DO_NOTHING, db_column='fid')
    designation = models.TextField()

    class Meta:
        managed = False
        db_table = 'faculty_designation'


class FacultyDetails(models.Model):
    fid = models.CharField(primary_key=True, max_length=50)
    name = models.TextField()
    deptname = models.CharField(max_length=100)
    phoneno = models.TextField()
    email = models.TextField()
    photo = models.TextField()

    class Meta:
        managed = False
        db_table = 'faculty_details'


class FeedbackIndex(models.Model):
    indexno = models.AutoField(primary_key=True)
    deptname = models.CharField(max_length=100)
    fid = models.CharField(max_length=50)
    subjectid = models.CharField(max_length=50)
    acdyear = models.CharField(max_length=10)
    indexmark = models.FloatField()
    classid = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'feedback_index'
        unique_together = (('indexno', 'deptname', 'fid', 'subjectid', 'indexmark'), ('indexno', 'deptname', 'fid', 'subjectid', 'indexmark'),)


class FeedbackStatus(models.Model):
    classid = models.CharField(primary_key=True, max_length=50)
    deptname = models.ForeignKey(Department, models.DO_NOTHING, db_column='deptname')
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'feedback_status'


class FeedbackStud(models.Model):
    studid = models.CharField(max_length=50)
    acdyear = models.CharField(max_length=10)
    subjectid = models.CharField(max_length=20)
    fid = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'feedback_stud'


class HostelStudReg(models.Model):
    admno = models.CharField(db_column='ADMNO', max_length=50)  # Field name made lowercase.
    parent_address = models.CharField(max_length=100)
    parent_mob = models.CharField(max_length=13)
    present_res_adress = models.CharField(max_length=100, blank=True, null=True)
    priority1 = models.IntegerField(blank=True, null=True)
    priority2a = models.IntegerField(blank=True, null=True)
    priority2d = models.IntegerField(blank=True, null=True)
    priority2e = models.IntegerField(blank=True, null=True)
    income = models.BigIntegerField(blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    sgpa = models.FloatField(blank=True, null=True)
    disci_action = models.CharField(max_length=55, blank=True, null=True)
    admn_status = models.CharField(max_length=15, blank=True, null=True)
    hos_rank = models.FloatField(blank=True, null=True)
    distance_metric = models.FloatField(blank=True, null=True)
    rank_metric = models.FloatField(blank=True, null=True)
    entrance_rank = models.IntegerField(db_column='Entrance_rank', blank=True, null=True)  # Field name made lowercase.
    sc = models.IntegerField(db_column='SC')  # Field name made lowercase.
    st = models.IntegerField(db_column='ST')  # Field name made lowercase.
    ph = models.IntegerField(db_column='PH')  # Field name made lowercase.
    bpl = models.IntegerField(db_column='BPL')  # Field name made lowercase.
    other_state = models.IntegerField()
    central = models.IntegerField(db_column='CENTRAL')  # Field name made lowercase.
    priority2b = models.IntegerField()
    priority2c = models.IntegerField()
    priority2f = models.IntegerField()
    final_rank = models.CharField(max_length=5, blank=True, null=True)
    remarks = models.CharField(max_length=50, blank=True, null=True)
    permanent_add = models.CharField(db_column='Permanent_add', max_length=100, blank=True, null=True)  # Field name made lowercase.
    permanent_mob = models.CharField(db_column='Permanent_mob', max_length=13, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=13, blank=True, null=True)
    postoffice = models.CharField(max_length=50, blank=True, null=True)
    acd_year = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    app_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hostel_stud_reg'


class LabBatch(models.Model):
    batch_id = models.AutoField(primary_key=True)
    batch_name = models.CharField(max_length=50)
    sub_code = models.ForeignKey('SubjectClass', models.DO_NOTHING, db_column='sub_code')
    classid = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'lab_batch'


class LabBatchStudent(models.Model):
    studid = models.CharField(max_length=50)
    batch = models.ForeignKey(LabBatch, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'lab_batch_student'


class LabBatchStudentold(models.Model):
    studid = models.CharField(max_length=50)
    batch_id = models.IntegerField()
    acd_year = models.TextField()
    classid = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'lab_batch_studentold'


class LabBatchold(models.Model):
    batch_id = models.IntegerField()
    batch_name = models.CharField(max_length=50)
    sub_code = models.CharField(max_length=50)
    acd_year = models.TextField()

    class Meta:
        managed = False
        db_table = 'lab_batchold'


class LastAdmNo(models.Model):
    ug = models.IntegerField()
    pg = models.IntegerField()
    phd = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'last_adm_no'


class Login(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=50)
    usertype = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'login'


class Mainfeedback(models.Model):
    deptname = models.CharField(max_length=50)
    semid = models.CharField(max_length=5)
    subjectid = models.CharField(max_length=20)
    acdyear = models.CharField(max_length=10)
    responseid = models.AutoField(primary_key=True)
    qs1 = models.FloatField()
    qs2 = models.FloatField()
    qs3 = models.FloatField()
    qs4 = models.FloatField()
    qs5 = models.FloatField()
    qs6 = models.FloatField()
    qs7 = models.FloatField()
    qs8 = models.FloatField()
    qs9 = models.FloatField()
    qs10 = models.FloatField()
    qs11 = models.FloatField()
    qs12 = models.TextField()
    fid = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'mainfeedback'


class Notification(models.Model):
    nid = models.BigAutoField(primary_key=True)
    data = models.TextField()
    send_id = models.CharField(max_length=50)
    rec_id = models.CharField(max_length=50)
    send_type = models.TextField()
    rec_type = models.TextField()
    date = models.TextField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'notification'


class Parent(models.Model):
    parentid = models.AutoField(primary_key=True)
    name_guard = models.TextField()
    guard_contactno = models.TextField()
    relation = models.TextField()
    occupation = models.TextField()
    guard_email = models.TextField()
    income = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'parent'


class ParentStudent(models.Model):
    psid = models.BigAutoField(primary_key=True)
    admissionno = models.ForeignKey('StudDetails', models.DO_NOTHING, db_column='admissionno')
    parentid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'parent_student'


class PgstudentQual(models.Model):
    admissionno = models.OneToOneField('StudDetails', models.DO_NOTHING, db_column='admissionno', primary_key=True)
    degree_course = models.TextField(blank=True, null=True)
    degree_regno = models.TextField(blank=True, null=True)
    degree_marks = models.IntegerField(blank=True, null=True)
    degree_percent = models.IntegerField(blank=True, null=True)
    college_name = models.CharField(max_length=50, blank=True, null=True)
    university = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pgstudent_qual'


class RitKeys(models.Model):
    key_id = models.AutoField(primary_key=True)
    key_email = models.CharField(max_length=255)
    key_username = models.CharField(max_length=255)
    key_key = models.CharField(max_length=255)
    key_remark = models.CharField(max_length=255, blank=True, null=True)
    key_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rit_keys'


class Scholarship(models.Model):
    schol = models.ForeignKey('ScholarshipType', models.DO_NOTHING)
    studid = models.ForeignKey('StudDetails', models.DO_NOTHING, db_column='studid')
    schol_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scholarship'


class ScholarshipType(models.Model):
    schol_name = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scholarship_type'


class Semregstatus(models.Model):
    curr_sem = models.CharField(max_length=50)
    next_sem = models.CharField(max_length=50)
    status = models.IntegerField()
    current_class = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'semregstatus'


class Serialno(models.Model):
    rcpt_no = models.AutoField(primary_key=True)
    classid = models.CharField(max_length=50)
    issued_by = models.CharField(max_length=20)
    issued_to = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'serialno'


class SessionalMarks(models.Model):
    classid = models.CharField(primary_key=True, max_length=50)
    studid = models.ForeignKey('StudDetails', models.DO_NOTHING, db_column='studid')
    subjectid = models.ForeignKey('SubjectClass', models.DO_NOTHING, db_column='subjectid')
    sessional_marks = models.FloatField()
    sessional_remark = models.TextField(blank=True, null=True)
    verification_status = models.IntegerField()
    sessional_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sessional_marks'
        unique_together = (('classid', 'studid', 'subjectid'),)


class SessionalMarksold(models.Model):
    classid = models.CharField(primary_key=True, max_length=50)
    studid = models.CharField(max_length=50)
    subjectid = models.CharField(max_length=50)
    sessional_marks = models.FloatField()
    sessional_remark = models.TextField(blank=True, null=True)
    verification_status = models.IntegerField()
    sessional_date = models.DateTimeField()
    acd_year = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sessional_marksold'
        unique_together = (('classid', 'studid', 'subjectid'),)


class SessionalStatus(models.Model):
    classid = models.CharField(max_length=50)
    subjectid = models.ForeignKey('SubjectClass', models.DO_NOTHING, db_column='subjectid')
    sessional_status = models.CharField(max_length=255)
    verification_status = models.IntegerField()
    sessional_remark = models.TextField(blank=True, null=True)
    sessional_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sessional_status'


class SessionalStatusold(models.Model):
    classid = models.CharField(max_length=50)
    subjectid = models.CharField(max_length=50)
    sessional_status = models.CharField(max_length=255)
    verification_status = models.IntegerField()
    sessional_remark = models.TextField(blank=True, null=True)
    sessional_date = models.DateTimeField()
    acd_year = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sessional_statusold'


class StaffAdvisor(models.Model):
    classid = models.CharField(primary_key=True, max_length=50)
    fid = models.ForeignKey(FacultyDetails, models.DO_NOTHING, db_column='fid')
    students_list = models.TextField()

    class Meta:
        managed = False
        db_table = 'staff_advisor'
        unique_together = (('classid', 'fid'),)


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


class StudSemRegistration(models.Model):
    reg_id = models.AutoField(primary_key=True)
    adm_no = models.CharField(max_length=10, blank=True, null=True)
    classid = models.CharField(max_length=50)
    apl_status = models.CharField(max_length=35)
    apl_date = models.DateField()
    apv_status = models.CharField(max_length=35)
    apv_date = models.DateField()
    batch_id = models.IntegerField()
    previous_sem = models.CharField(max_length=4, blank=True, null=True)
    new_sem = models.CharField(max_length=4, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    form_data = models.TextField(blank=True, null=True)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'stud_sem_registration'


class StudSemRegistrationold(models.Model):
    reg_id = models.AutoField(primary_key=True)
    adm_no = models.CharField(max_length=10)
    classid = models.CharField(max_length=50)
    apl_status = models.CharField(max_length=35)
    apl_date = models.DateField()
    apv_status = models.CharField(max_length=35)
    apv_date = models.DateField()
    batch_id = models.IntegerField()
    previous_sem = models.CharField(max_length=4)
    new_sem = models.CharField(max_length=4)
    remarks = models.TextField()
    form_data = models.TextField()
    date = models.DateTimeField()
    acd_year = models.TextField()

    class Meta:
        managed = False
        db_table = 'stud_sem_registrationold'


class SubjectAllocation(models.Model):
    classid = models.OneToOneField('SubjectClass', models.DO_NOTHING, db_column='classid', primary_key=True)
    subjectid = models.ForeignKey('SubjectClass', models.DO_NOTHING, db_column='subjectid')
    fid = models.ForeignKey(FacultyDetails, models.DO_NOTHING, db_column='fid')
    type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'subject_allocation'
        unique_together = (('classid', 'subjectid', 'fid', 'type'),)


class SubjectAllocationold(models.Model):
    classid = models.CharField(primary_key=True, max_length=50)
    subjectid = models.CharField(max_length=50)
    fid = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    acd_year = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'subject_allocationold'
        unique_together = (('classid', 'subjectid', 'fid', 'type', 'acd_year'),)


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


class SubjectClassold(models.Model):
    subjectid = models.CharField(primary_key=True, max_length=50)
    subject_title = models.TextField()
    classid = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'subject_classold'
        unique_together = (('subjectid', 'classid'),)


class Tc(models.Model):
    tc_no = models.AutoField(primary_key=True)
    adm_no = models.CharField(max_length=10)
    tc_date = models.TextField()
    reason = models.TextField()

    class Meta:
        managed = False
        db_table = 'tc'


class Temp(models.Model):
    temp_no = models.BigIntegerField(primary_key=True)
    name = models.TextField()
    dob = models.DateField()
    gender = models.TextField()
    religion = models.TextField()
    caste = models.TextField()
    year_of_admission = models.IntegerField()
    email = models.TextField()
    mobile_phno = models.TextField()
    land_phno = models.TextField()
    address = models.TextField()
    rollno = models.TextField()
    rank = models.IntegerField()
    quota = models.TextField()
    school_1 = models.TextField()
    regno_1 = models.TextField()
    board_1 = models.TextField()
    percentage_1 = models.FloatField()
    school_2 = models.TextField()
    regno_2 = models.TextField()
    board_2 = models.TextField()
    percentage_2 = models.FloatField()
    no_chance1 = models.TextField()
    courseid = models.CharField(max_length=50)
    branch_or_specialisation = models.CharField(max_length=100)
    image = models.TextField()
    gate_score = models.IntegerField(blank=True, null=True)
    admission_type = models.CharField(max_length=30)
    entry_sem = models.IntegerField()
    exit_sem = models.IntegerField(blank=True, null=True)
    blood = models.CharField(max_length=5)
    name_guardian = models.TextField()
    relation = models.TextField()
    occupation = models.TextField()
    income = models.IntegerField()
    guard_contactno = models.TextField()
    guard_email = models.TextField()
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    maths = models.IntegerField()
    total_marks = models.IntegerField()
    percentage = models.FloatField()
    school_3 = models.TextField()
    degree_course = models.CharField(max_length=50)
    degree_regno = models.CharField(max_length=50)
    degree_marks = models.IntegerField()
    degree_percent = models.FloatField(blank=True, null=True)
    board_3 = models.TextField()
    status = models.CharField(max_length=50)
    last_institution = models.TextField()
    tc_no_adm = models.CharField(max_length=100)
    tc_date_adm = models.DateField()

    class Meta:
        managed = False
        db_table = 'temp'


class UgstudentQual(models.Model):
    admissionno = models.OneToOneField(StudDetails, models.DO_NOTHING, db_column='admissionno', primary_key=True)
    physics = models.TextField(blank=True, null=True)
    chemistry = models.TextField(blank=True, null=True)
    maths = models.TextField(blank=True, null=True)
    total_marks = models.IntegerField(blank=True, null=True)
    percentage = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ugstudent_qual'


class UniversityMark(models.Model):
    semester = models.CharField(max_length=50)
    registerno = models.IntegerField()
    subject_code = models.CharField(max_length=100)
    mark = models.CharField(max_length=50)
    studid = models.CharField(max_length=50)
    status = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'university_mark'
