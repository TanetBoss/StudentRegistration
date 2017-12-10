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

class History(models.Model):
    his_student_FK = models.ForeignKey(Student, on_delete=models.CASCADE)
    his_subject_FK = models.ForeignKey(Subject, on_delete=models.CASCADE)
    StudyYet = models.BooleanField()
    Grade = models.CharField(max_length=2)

    def __str__(self):
        return self.his_student_FK.name + '--' + self.his_subject_FK.SubjectName
