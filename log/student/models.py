from django.db import models
from django.urls import reverse
import datetime

# Create your models here.

class Department(models.Model):
    DepNo = models.CharField(max_length = 4, default='xxxx')
    DepName = models.CharField(max_length = 30)
    DepTel = models.CharField(max_length=12)
    DepEmail = models.CharField(max_length = 50)
    DepHead = models.CharField(max_length = 11)
    Dep_logo = models.ImageField()

    def get_absolute_url(self):
        return reverse('student:detail', kwargs = {'pk': self.pk})

    def __str__(self):
        return self.DepNo + '--' + self.DepName

class Curriculum(models.Model):
    cur_dep_FK = models.ForeignKey(Department, on_delete = models.CASCADE)
    cCurriculum = models.CharField(max_length = 30)

    def __str__(self):
        return self.cur_dep_FK.DepName + '--' + self.cCurriculum

class Credit(models.Model):
    cre_cur_FK = models.ForeignKey(Curriculum, on_delete = models.CASCADE)
    thYear = models.CharField(max_length = 1, default = '-')
    CreditRequire = models.IntegerField()
    Semester = models.CharField(max_length = 20, default='X/YYYY')

    def __str__(self):
        return self.cre_cur_FK.cCurriculum + '--' + 'yr' + self.thYear + '--' + self.Semester

class Lecturer(models.Model):
    lec_dep_FK = models.ForeignKey(Department, on_delete = models.CASCADE, default='DEP')
    LecturerID = models.CharField(max_length = 11)
    LecturerDegree = models.CharField(max_length=20)
    LecturerName = models.CharField(max_length = 50)
    LecturerAddress = models.CharField(max_length = 100, default=None, blank=True, null=True)
    LecturerTel = models.CharField(max_length = 12, default=None, blank=True, null=True)
    LecturerRating = models.FloatField(default=None, blank=True, null=True)
    LecturerEmail = models.CharField(max_length = 50, default=None, blank=True, null=True)
    LecturerProfile = models.ImageField()

    def get_absolute_url(self):
        return reverse('student:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.LecturerName

class LecturerResearch(models.Model):
    research_lec_FK = models.ForeignKey(Lecturer,on_delete=models.CASCADE)
    ResearchName = models.CharField(max_length=30)
    Category =	models.CharField(max_length=20)
    Description = models.CharField(max_length=150)


    def get_absolute_url(self):
        return reverse('student:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.ResearchName + ' -- ' + self.Category

class Student(models.Model):
    stu_dep_FK = models.ForeignKey(Department, on_delete = models.CASCADE, default='DEP')
    StudentID = models.CharField(max_length=11)
    Degree = models.CharField(max_length = 20, default='DEG')
    name = models.CharField(max_length = 50, default='NAME')
    DOB = models.DateField()
    Tel = models.CharField(max_length = 12, default='TEL', blank=True, null=True)
    Email = models.CharField(max_length = 12, default=None, blank=True, null=True)
    GPAX = models.FloatField(null=True)
    Address = models.CharField(max_length = 100, default=None, blank=True, null=True)
    Status = models.CharField(max_length = 20, default='Normal')
    CurrentSemester = models.CharField(max_length = 20, default='X/YYYY')
    Curriculum = models.CharField(max_length = 20, default='CURRICULUM NAME')

    def __str__(self):
        return self.name

class Register(models.Model):
    RegNo = models.CharField(max_length=15)
    Date = models.DateField()
    reg_stu_FK = models.ForeignKey(Student, on_delete = models.CASCADE)
    Cost = models.FloatField()
    Discount = models.FloatField()
    PaymentMethod = models.CharField(max_length = 10)
    PaymentStatus = models.CharField(max_length = 10)
    PaymentDate = models.DateField(default=None, blank=True, null=True)
    Semester = models.CharField(max_length = 20, default='X/YYYY')

    def __str__(self):
        return self.RegNo


class Advisor(models.Model):
    adv_stu_FK = models.ForeignKey(Student, on_delete = models.CASCADE)
    adv_lec_FK = models.ForeignKey(Lecturer, on_delete = models.CASCADE)
    order = models.IntegerField()
    def __str__(self):
        return self.adv_stu_FK.name + '--'+ self.adv_lec_FK.LecturerName + '--' + str(self.order)

class Subject(models.Model):
    sub_sec_FK = models.ForeignKey('Section', on_delete=models.CASCADE, blank=True, null=True)
    SubjectID = models.CharField(max_length=8)
    SubjectName = models.CharField(max_length=30)
    Prerequisite = models.CharField(max_length=8, default=None, blank=True, null=True)
    Semester = models.CharField(max_length = 20, default='X/YYYY')
    Credit = models.IntegerField(default=3)

    def __str__(self):
        return self.SubjectName

class Section(models.Model):
    sec_subject_FK = models.ForeignKey(Subject, on_delete=models.CASCADE,default=None, blank=True, null=True)
    SectionNo = models.CharField(max_length=2)
    TotalSeat = models.IntegerField()
    LessonTime = models.CharField(max_length=20)

    def __str__(self):
        return self.SectionNo

class LecturerInSection(models.Model):
    lecsec_sub_FK = models.ForeignKey(Subject, on_delete = models.CASCADE)
    lecsec_sec_FK = models.ForeignKey(Section, on_delete = models.CASCADE)
    lecsec_lec_FK = models.ForeignKey(Lecturer, on_delete = models.CASCADE)
    order = models.IntegerField()

    def __str__(self):
        return self.lecsec_lec_FK.LecturerName + '--' + self.lecsec_sub_FK.SubjectName + '--' + self.lecsec_sec_FK.SectionNo + '--' + str(self.order)

class History(models.Model):
    his_student_FK = models.ForeignKey(Student, on_delete=models.CASCADE)
    his_subject_FK = models.ForeignKey(Subject, on_delete=models.CASCADE)
    StudyYet = models.BooleanField()
    Grade = models.CharField(max_length=2)

    def __str__(self):
        return self.his_student_FK.name + '--' + self.his_subject_FK.SubjectName
