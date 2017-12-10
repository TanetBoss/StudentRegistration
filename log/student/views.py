from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import  authenticate,login
from django.urls import reverse_lazy
from django.views.generic import View
from .models import Department, Student, Subject, History
from login.forms import UserForm


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


class IndexView(generic.ListView):
    template_name = 'student/index.html'
    context_object_name = 'all_departments'

    def get_queryset(self):
        return Department.objects.all()


class StudentIndexView(generic.ListView):
    template_name = 'student/Sindex.html'
    context_object_name = 'all_students'

    def get_queryset(self):
        return Student.objects.all()


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
