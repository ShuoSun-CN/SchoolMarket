
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from djangoProject2.settings import MEDIA_ROOT
from login.views import urlpatterns_view
from login.utils import login,stu_list
from GoodMarket.urls import gm_urlpattrens
urlpatterns = [
    path('admin/', admin.site.urls),
    path('verify_login/',login.verify_login),
    path('verify_register/',login.verify_register),
    path('sendCode/',login.send_register_code),
    path('get_student_record/',stu_list.get_stu_list),
    path('delete_student_record/',stu_list.delete_stu_list),
    path('add_student_record/',stu_list.add_stu_list),
    path('query_student_record/',stu_list.query_stu_list),
    path('getUserInfo/',login.getUserInfo),
    path('modify_student_record/',stu_list.modify_stu_list),
]+urlpatterns_view+static('/good_image/',document_root=MEDIA_ROOT+'/good_image/')+gm_urlpattrens
