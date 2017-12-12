from django.contrib import admin
from .models import Department, Student, Subject, History, Section, Lecturer, Advisor, LecturerInSection, LecturerResearch, Curriculum, Register, Credit
# Register your models here.

admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(History)
admin.site.register(Section)
admin.site.register(Lecturer)
admin.site.register(Advisor)
admin.site.register(LecturerInSection)
admin.site.register(LecturerResearch)
admin.site.register(Curriculum)
admin.site.register(Register)
admin.site.register(Credit)
