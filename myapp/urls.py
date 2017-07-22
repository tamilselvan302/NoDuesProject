from django.conf.urls import url
from . import views

app_name = 'myapp'

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^hostel/$', views.hostel,name='hostel'),
    url(r'^Login/$', views.Login.as_view(),name='Login'),
    url(r'^comment/$', views.comment,name='comment'),
    url(r'^successEdit/$', views.successEdit,name='successEdit'),
    url(r'^Logout/$', views.Logout,name='Logout'),

    url(r'^others/$', views.others,name='others'),
    url(r'^otherscomment/$', views.otherscomment,name='otherscomment'),
    url(r'^successEditothers/$', views.successEditothers,name='successEditothers'),

    url(r'^stud1/$', views.stud1,name='stud1'),
    url(r'^stud2/$', views.stud2,name='stud2'),

]