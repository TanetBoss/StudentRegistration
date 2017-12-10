from django.conf.urls import url
from . import views

app_name = 'student'

urlpatterns = [

    url(r'^$',views.IndexView.as_view(), name ='index'),

    url(r'^avgdep/$', views.AVGdepartment, name='avg-dep'),

    url(r'^students/$', views.StudentIndex, name='Sindex'),

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

    url(r'^lindex/$', views.LIndexView.as_view(), name='Lindex'),
    url(r'^lindex/(?P<pk>[0-9]+)/$',views.LDetailView.as_view(), name='Ldetail'),
    url(r'lecturer/lindex/add/$',views.LecturerCreate.as_view(), name='lecturer-add'),
    url(r'research/lindex/add/$',views.ResearchCreate.as_view(), name='research-add'),
    url(r'lecturer/lindex/(?P<pk>[0-9]+)/$', views.LecturerUpdate.as_view(), name='lecturer-update'),
    url(r'research/lindex/(?P<pk>[0-9]+)/$', views.ResearchUpdate.as_view(), name='research-update'),
    url(r'research/lindex/(?P<pk>[0-9]+)/delete/$', views.ResearchDelete.as_view(), name='research-delete'),
    url(r'lecturer/lindex/(?P<pk>[0-9]+)/delete/$', views.LecturerDelete.as_view(), name='lecturer-delete'),
]
