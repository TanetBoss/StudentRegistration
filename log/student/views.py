from django.views import generic
from django.http import HttpResponse
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import  authenticate,login
from django.urls import reverse_lazy
from django.views.generic import View
from .models import Department, Student, Subject, History, LecturerInSection, Register
from .models import Lecturer
from .models import LecturerResearch
from login.forms import UserForm
from django.db.models import Count


class Home(generic.ListView):
    template_name = 'student/home.html'
    def get_queryset(self):
        return Department.objects.all()

class StudentFormView(generic.ListView):
    template_name = 'student/complex-form.html'

    def get_queryset(self):
        return History.objects.all()

class StudentManageView(generic.ListView):
    template_name = 'student/studentmanage.html'

    def get_queryset(self):
        return Subject.objects.all()

def AVGdepartment(request):
    header_str = Student.objects.all()
    template = loader.get_template('student/avg-department.html')
    b = Department.objects.all()
    count = b.count()
    sum = 0
    current = 0
    list = []
    divide = []
    departmentname = []

    for a in range(count):
        list.append(0)
        divide.append(0)
        departmentname.append(0)

    for department in Department.objects.all():
        for student in header_str:
            if student.stu_dep_FK.DepName == department.DepName :
                departmentname[current] = department.DepName
                list[current] = list[current] + student.GPAX
                divide[current] = divide[current] + 1
        current = current + 1

    for a in range(count):
        list[a] = list[a] / divide[a]

    context = {
        'count': count,
        'department_list': Department.objects.all(),
        'departmentname': departmentname,
        'list': list,
        'header_str': header_str,
    }

    return HttpResponse(template.render(context, request))

def totalCostDep(request):
    header_str = Student.objects.all()
    regis_str = Register.objects.all()
    template = loader.get_template('student/totalCost-form.html')
    b = Department.objects.all()
    count = b.count()
    sum = 0
    current = 0
    debugger = 0
    list = []
    departmentname = []
    debugger = []

    for a in range(count):
        list.append(0)
        departmentname.append(0)
        debugger.append(0)

    for department in Department.objects.all():
        for regis in regis_str:
            if regis.reg_stu_FK.stu_dep_FK.DepName == department.DepName:
                departmentname[current] = department.DepName
                list[current] = list[current] + regis.Cost

                debugger[current] = debugger[current] + 1
        current = current + 1

    context = {
        'debug': debugger,
        'count': count,
        'department_list': Department.objects.all(),
        'departmentname': departmentname,
        'list': list,
        'header_str': header_str,
    }

    return HttpResponse(template.render(context, request))

def totalCostLec(request):
    header_str = Student.objects.all()
    lec_str = Lecturer.objects.all()
    template = loader.get_template('student/totalCost-lec.html')
    b = Department.objects.all()
    count = b.count()
    sum = 0
    current = 0
    debugger = 0
    list = []
    departmentname = []
    debugger = []

    for a in range(count):
        list.append(0)
        departmentname.append(0)
        debugger.append(0)

    for department in Department.objects.all():
        for lecturer in lec_str:
            if lecturer.lec_dep_FK.DepName == department.DepName:
                departmentname[current] = department.DepName
                list[current] = list[current] + 1

                debugger[current] = debugger[current] + 1
        current = current + 1

    context = {
        'debug': debugger,
        'count': count,
        'department_list': Department.objects.all(),
        'departmentname': departmentname,
        'list': list,
        'header_str': header_str,
    }

    return HttpResponse(template.render(context, request))

def ResearchCount(request):
    research_str = LecturerResearch.objects.all()
    template = loader.get_template('student/researchcount-form.html')
    extractResearch = LecturerResearch.objects.values('Category').annotate(dcount=Count('Category'))
    lex = list(extractResearch)

    nR = list()
    cR = list()

    for d in lex:
        nR.append(d['dcount'])
    for d in lex:
        cR.append(d['Category'])



    context = {
        'count' :nR,
        'Rname' :cR,
    }

    return HttpResponse(template.render(context, request))


class IndexView(generic.ListView):
    template_name = 'student/index.html'
    context_object_name = 'all_departments'

    def get_queryset(self):
        return Department.objects.all()


def StudentIndex(request):
    all_students = Student.objects.all()

    query = request.GET.get("q")
    if query:
        all_students = all_students.filter(name__icontains=query)

    return render(request, 'student/Sindex.html',{'all_students': all_students})


class StudentCreate(CreateView):
    model = Student
    fields = ['stu_dep_FK', 'name', 'Degree', 'DOB', 'Tel']
    success_url = reverse_lazy('student:index')

class StudentUpdate(UpdateView):
    model = Student
    fields = ['stu_dep_FK', 'name', 'Degree', 'DOB', 'Tel']
    success_url = reverse_lazy('student:index')

class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('student:Sindex')

class DetailView(generic.DetailView):
    model = Department
    template_name = 'student/detail.html'


class DepartmentCreate(CreateView):
    model = Department
    fields = ['DepName', 'DepHead', 'DepTel', 'DepEmail', 'Dep_logo']


class DepartmentUpdate(UpdateView):
    model = Department
    fields = ['DepName', 'DepHead', 'DepTel', 'DepEmail', 'Dep_logo']


class DepartmentDelete(DeleteView):
    model = Department
    success_url = reverse_lazy('student:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'student/registration_form.html'
    # display blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    # process form data
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return User objects if credentials are correct
            user = authenticate(username=username,password=password)

            if user is not None:

                if user.is_active:
                    login(request,user)
                    return redirect('student:index')
        return render(request,self.template_name,{'form':form})



class LIndexView(generic.ListView):
    template_name = 'student/Lindex.html'
    context_object_name = 'all_lecturers'
    def get_queryset(self):
        return Lecturer.objects.all()


class LDetailView(generic.DetailView):
    model = Lecturer
    template_name = 'student/Ldetail.html'


class LecturerCreate(CreateView):
    model = Lecturer
    fields = ['lec_dep_FK','LecturerID','LecturerDegree','LecturerName','LecturerAddress','LecturerTel','LecturerEmail','LecturerProfile']
    success_url = reverse_lazy('student:Lindex')

class LecturerUpdate(UpdateView):
    model = Lecturer
    fields = ['lec_dep_FK','LecturerID','LecturerDegree','LecturerName','LecturerAddress','LecturerTel','LecturerEmail','LecturerProfile']
    success_url = reverse_lazy('student:Lindex')

class LecturerDelete(DeleteView):
    model = Lecturer
    success_url = reverse_lazy('student:Lindex')


class ResearchCreate(CreateView):
    model = LecturerResearch
    fields = ['research_lec_FK', 'ResearchName', 'Category', 'Description']
    success_url = reverse_lazy('student:Lindex')


class ResearchDelete(DeleteView):
    model = LecturerResearch
    success_url = reverse_lazy('student:Lindex')

class ResearchUpdate(UpdateView):
    model = LecturerResearch
    fields = ['research_lec_FK', 'ResearchName', 'Category', 'Description']
    success_url = reverse_lazy('student:Lindex')


class CourseCreate(CreateView):
    model = Subject
    fields = ['sub_sec_FK', 'SubjectID', 'SubjectName', 'Prerequisite', 'Semester', 'Credit']
    success_url = reverse_lazy('student:Lindex')

class AssignLecturer(CreateView):
    model = LecturerInSection
    fields = ['lecsec_sub_FK', 'lecsec_sec_FK', 'lecsec_lec_FK', 'order']
    success_url = reverse_lazy('student:Lindex')
