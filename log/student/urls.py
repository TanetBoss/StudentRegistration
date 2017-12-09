from django.conf.urls import url
from . import views

app_name = 'student'

urlpatterns = [

    url(r'^$',views.IndexView.as_view(), name ='index'),

    url(r'^studentform/$', views.StudentFormView.as_view(), name='studentform'),

    url(r'^studentmanage/$', views.StudentManageView.as_view(), name='student-manage'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail' ),

    url(r'department/add/$',views.DepartmentCreate.as_view(), name='department-add'),

    url(r'department/(?P<pk>[0-9]+)/$', views.DepartmentUpdate.as_view(), name='department-update'),

    url(r'department/(?P<pk>[0-9]+)/delete/$', views.DepartmentDelete.as_view(), name='department-delete'),
]
