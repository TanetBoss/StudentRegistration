from django.db import models
from django.urls import reverse

# Create your models here.

class Department(models.Model):
    DepName = models.CharField(max_length = 50)
    DepHead = models.CharField(max_length = 100)
    DepTel = models.CharField(max_length=20)
    DepEmail = models.CharField(max_length = 500)
    Dep_logo = models.ImageField()

    def get_absolute_url(self):
        return reverse('student:detail', kwargs = {'pk': self.pk})

    def __str__(self):
        return self.DepName

class Student(models.Model):
    department = models.ForeignKey(Department, on_delete = models.CASCADE, default='DEP')
    StudentID = models.CharField(max_length=10, default='xxxxxxxxxx')
    name = models.CharField(max_length = 200, default='NAME')
    Degree = models.CharField(max_length = 200, default='DEG')
    DOB = models.CharField(max_length = 200, default='DEF')
    Tel = models.CharField(max_length = 200, default='TEL')
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Subject(models.Model):
    subjectFK = models.ForeignKey(Student, on_delete=models.CASCADE)
    SubjectID = models.CharField(max_length=10)
    SubjectName = models.CharField(max_length=30)
    Section = models.CharField(max_length=2)

    def __str__(self):
        return self.SubjectName
