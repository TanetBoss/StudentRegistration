from django.conf.urls import url
from . import views

app_name = 'student'

urlpatterns = [

    url(r'^$',views.IndexView.as_view(), name ='index'),

<<<<<<< HEAD
    url(r'^avgdep/$', views.AVGdepartment, name='avg-dep'),

    url(r'^students/$', views.StudentIndexView.as_view(), name='Sindex'),
=======
    url(r'^students/$', views.StudentIndex, name='Sindex'),
>>>>>>> 85d1b5bc888f5fc16bd121907cc96e393bb635d6

    url(r'^studentform/$', views.StudentFormView.as_view(), name='studentform'),

    url(r'^studentmanage/$', views.StudentManageView.as_view(), name='student-manage'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail' ),

    url(r'student/add/$', views.StudentCreate.as_view(), name='student-add'),

    url(r'student/(?P<pk>[0-9]+)/$', views.StudentUpdate.as_view(), name='student-update'),

    url(r'student/(?P<pk>[0-9]+)/delete/$', views.StudentDelete.as_view(), name='student-delete'),

    url(r'department/add/$',views.DepartmentCreate.as_view(), name='department-add'),

    url(r'department/(?P<pk>[0-9]+)/$', views.DepartmentUpdate.as_view(), name='department-update'),

    url(r'department/(?P<pk>[0-9]+)/delete/$', views.DepartmentDelete.as_view(), name='department-delete'),
]
