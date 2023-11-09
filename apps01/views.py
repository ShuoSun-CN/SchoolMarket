from django.shortcuts import render,redirect
import psycopg2
# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect,render
from django.views.decorators.csrf import csrf_exempt

def login(req):
    if 'user_verify'in req.COOKIES:
        return redirect('/index')
    else:
        print(req.COOKIES)
        return render(req,"page-login.html")
def logout(req):
    response=redirect('/')
    response.delete_cookie('user_verify')
    return response


def register(request):
    return render(request,"page-register.html")

def index(req):
    return render(req,"index.html")
def stu_manage(req):
    return render(req,"student_manage.html")
def MyOrders(req):
    return render(req,"mygoods.html")
def MyGoods(req):
    return render(req,"myorders.html")
def forgetpassword(req):
    return render(req,"page-forgot-password.html")