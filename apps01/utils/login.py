from django.shortcuts import render
import psycopg2
# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect,render
from django.views.decorators.csrf import csrf_exempt


def connect_db():
    try:
        conn=psycopg2.connect(database="postgres",user="postgres",password="123",host="localhost",port="5432")
    except Exception as e:
        print("Database connect failed!",e)
    else:
        return conn
    return None

@csrf_exempt
def verify_login(request):
    db=connect_db()
    if db is None:
        return JsonResponse(
            {"code":2}
        )
    condb=db.cursor()
    user_id=request.POST.get("user_id")
    password=request.POST.get("password")
    condb.execute("select password from login_users where user_id="+'\''+user_id+'\'');

    try:
        db_password=condb.fetchall()[0][0].strip()
    except:
        db_password=None

    if db_password==password:
        response=JsonResponse({"code":0
        })
        response.set_cookie('user_verify',user_id,60*60*24*10)

        return response
    else:
        return JsonResponse(
            {"code":1}
        )

@csrf_exempt
def getUserInfo(req):
    db=connect_db()
    if db is None:
        return JsonResponse(
            {"code":2}
        )
    try:
        user_id=req.COOKIES['user_verify']
        condb = db.cursor()
        condb.execute("select sno from login_users where user_id=" + '\'' + user_id + '\'')
        sno = condb.fetchall()[0][0].strip()
        condb.execute("select sname from student where sno=" + '\'' + sno + '\'')
        sname=condb.fetchall()[0][0].strip()
        return JsonResponse({
            "code":0,
            "sname":sname
        })
    except Exception as e:
        print(e)
        return  JsonResponse(
            {
                "code":1
            }
        )