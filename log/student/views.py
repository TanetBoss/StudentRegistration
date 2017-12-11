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

class StudentManageView(generic.ListView):
    template_name = 'student/studentmanage.html'
    context_object_name = 'all_student'

    def get_queryset(self):
        return Student.objects.all()

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
            departmentname[current] = department.DepName
            if student.stu_dep_FK.DepName == department.DepName :
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
            departmentname[current] = department.DepName
            if regis.reg_stu_FK.stu_dep_FK.DepName == department.DepName:
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
            departmentname[current] = department.DepName
            if lecturer.lec_dep_FK.DepName == department.DepName:
                list[current] = list[current] + 1
        current = current + 1

    context = {
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


def StudentFormView(request):
    reg_str = Register.objects.order_by('RegNo')
    template = loader.get_template('student/complex-form.html')
    count = reg_str.count()
    forboss = 0
    loop_str = ''
    looping = 0
    buttonbool = True
    liststudentID = []
    listregNo = []
    listdep = []
    listprice = []
    listdiscount = []
    liststatus = []
    lstudentID = []
    lregNo = []
    ldep = []
    lprice = []
    ldiscount = []
    lstatus = []

    username = None
    if request.user.is_authenticated():
        username = request.user.username

    for a in range(count):
        liststudentID.append(0)
        listregNo.append(0)
        listdep.append(0)
        listprice.append(0)
        listdiscount.append(0)
        liststatus.append(0)
        lstudentID.append(0)
        lregNo.append(0)
        ldep.append(0)
        lprice.append(0)
        ldiscount.append(0)
        lstatus.append(0)

    for reg in reg_str:
        liststudentID[looping] = reg.reg_stu_FK.StudentID
        listregNo[looping] = reg.RegNo
        listdep[looping] = reg.reg_stu_FK.stu_dep_FK.DepName
        listprice[looping] = reg.Cost
        listdiscount[looping] = reg.Discount
        liststatus[looping] = reg.PaymentStatus
        looping = looping + 1

    for reg in reg_str:
        if username == reg.reg_stu_FK.StudentID:
            lstudentID.append(reg.reg_stu_FK.StudentID)
            lregNo.append(reg.RegNo)
            ldep.append(reg.reg_stu_FK.stu_dep_FK.DepName)
            lprice.append(reg.Cost)
            ldiscount.append(reg.Discount)
            lstatus.append(reg.PaymentStatus)
            if reg.Semester == reg.reg_stu_FK.CurrentSemester and reg.PaymentStatus == 'Y': #find current semester in his/her history
                buttonbool = False
            forboss = forboss + 1

    for a in range(count):
        lstudentID.remove(0)
        lregNo.remove(0)
        ldep.remove(0)
        lprice.remove(0)
        ldiscount.remove(0)
        lstatus.remove(0)

    for a in range(forboss):
        loop_str = loop_str + 'x'

    context = {
        'loop_str':loop_str,
        'count':count,
        'buttonbool':buttonbool,
        'liststudentID':lstudentID,
        'listregNo':lregNo,
        'listdep':ldep,
        'listprice':lprice,
        'listdiscount':ldiscount,
        'liststatus':lstatus,
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
    fields = ['stu_dep_FK', 'name', 'Degree', 'DOB', 'Tel','StudentProfile']
    success_url = reverse_lazy('student:index')

class StudentUpdate(UpdateView):
    model = Student
    fields = ['stu_dep_FK', 'name', 'Degree', 'DOB', 'Tel','StudentProfile']
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


class CIndexView(generic.ListView):
    template_name = 'student/Courseindex.html'
    context_object_name = 'all_subjects'

    def get_queryset(self):
        return Subject.objects.all()

class CDetailView(generic.DetailView):
    model = Subject
    template_name = 'student/courseDetail.html'


class HistoryUpdate(UpdateView):
    model = History
    fields = ['Grade']
    success_url = reverse_lazy('student:Cindex')


class CourseUpdate(UpdateView):
    model = Subject
    fields = ['sub_sec_FK', 'SubjectID', 'SubjectName', 'Prerequisite', 'Semester', 'Credit']
    success_url = reverse_lazy('student:Cindex')

class CourseDelete(DeleteView):
    model = Subject
    success_url = reverse_lazy('student:Cindex')

class StudentHistory(generic.ListView):
    template_name = 'student/history.html'
    context_object_name = 'all_student'

    def get_queryset(self):
        return Student.objects.all()

class HistoryDetail(generic.DetailView):
    model = History
    template_name = 'student/history-detail.html'

class HistoryDelete(DeleteView):
    model = History
    success_url = reverse_lazy('student:Cindex')

class AddSubject(generic.ListView):
    template_name = 'student/add-subject.html'
    context_object_name = 'all_student'

    def get_queryset(self):
        return Student.objects.all()

class SubjectUpdate(UpdateView):
    model = History
    fields = ['StudyYet']
    success_url = reverse_lazy('student:Test')

class SDetailView(generic.ListView):
    template_name = 'student/StudentProfile.html'
    context_object_name = 'all_students'
    def get_queryset(self):
        return Student.objects.all()

class Test(generic.ListView):
    template_name = 'student/TestCart.html'
    context_object_name = 'all_student'

    def get_queryset(self):
        return Student.objects.all()

class RegisterUpdate(UpdateView):
    model = Register
    fields = ['PaymentMethod', 'PaymentStatus']
    success_url = reverse_lazy('student:studentform')
