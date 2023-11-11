"""
URL configuration for djangoProject2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps01 import views
from apps01.utils import login,stu_list
urlpatterns = [
    path('logout',views.logout),
    path('admin/', admin.site.urls),
    path('',views.login),
    path('index/',views.index),
    path('student_manage/',views.stu_manage),
    path('verify_login/',login.verify_login),
    path('verify_register/',login.verify_register),
    path('MyGoods/',views.MyGoods),
    path('MyOrders/',views.MyOrders),
    path('register/',views.register),
    path('forgetpassword/',views.forgetpassword),
    path('sendCode/',login.send_register_code),





    path('get_student_record/',stu_list.get_stu_list),
    path('delete_student_record/',stu_list.delete_stu_list),
    path('add_student_record/',stu_list.add_stu_list),
    path('query_student_record/',stu_list.query_stu_list),
    path('getUserInfo/',login.getUserInfo),
    path('modify_student_record/',stu_list.modify_stu_list)
]
