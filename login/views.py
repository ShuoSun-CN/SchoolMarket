from django.shortcuts import render,redirect
import psycopg2
# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect,render
from django.views.decorators.csrf import csrf_exempt
from django.urls import path


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
def goodMarket(req):
    return render(req,"good_market.html")
def forgetpassword(req):
    return render(req,"page-forgot-password.html")
def cart(req):
    return render(req,"cart.html")
urlpatterns_view=[
    path('logout', logout),
    path('MyGoods/', MyGoods),
    path('MyOrders/', MyOrders),
    path('register/', register),
    path('goodMarket/', goodMarket),
    path('index/', index),
    path('', login),
    path('forgetpassword/', forgetpassword),
    path('student_manage/', stu_manage),
    path('Cart/',cart)

]
