from django.urls import re_path
from basicapp import views


app_name='basicapp'

urlpatterns = [
    re_path(r'^relative/$', views.relative, name ='relative'),
    re_path(r'^other/$', views.other, name ='other')

]