from django.contrib import admin
from .models import Department, Student, Subject, History
# Register your models here.

admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(History)
