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
    department = models.ForeignKey(Department, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    Degree = models.CharField(max_length = 200)
    DOB = models.CharField(max_length = 200)
    Tel = models.CharField(max_length = 200)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.name

