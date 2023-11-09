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
def modify_stu_list(request):
    db=connect_db()

    if db is None:
        return JsonResponse(
            {"code":2}
        )
    print("链接数据库成功!")
    try:
        or_sno=request.POST.get('or_sno')
        sno=request.POST.get('sno')
        sname = request.POST.get('sname')
        sage = request.POST.get('sage')
        sgender = request.POST.get('sgender')
        sdept = request.POST.get('sdept')
        condb = db.cursor()

        condb.execute("update  student  set sno="+'\''+sno+'\','+'sname=\''+sname+'\','+'sgender=\''+sgender+'\',sage='+sage+','+'sdept=\''+sdept+'\''+"where sno="+'\''+or_sno+'\'')

        db.commit()

        print("执行sql:"+"update  student  set sno="+'\''+sno+'\','+'sname=\''+sname+'\','+'sgender=\''+sgender+'\',sage='+sage+','+'sdept=\''+sdept+'\''+"where sno="+'\''+or_sno+'\''+"成功!")
        return JsonResponse(
        {
                "code":0
            }
        )
    except Exception as e:
        print(e)
        return JsonResponse(
            {
                "code":1
            }
        )


@csrf_exempt
def query_stu_list(request):
    db=connect_db()

    if db is None:
        return JsonResponse(
            {"code":2}
        )
    print("链接数据库成功!")
    try:
        sno=request.POST.get('sno')
        condb=db.cursor()

        condb.execute("select * from student where sno="+'\''+sno+'\'')
        result=condb.fetchall()
        stu={}
        for stu in result:
            stu={
                "code":0,
                'sno': stu[0],
                'sname': stu[1],
                'sgender': stu[2],
                'sage': stu[3],
                'sdept': stu[4]
            }
            break


        return JsonResponse(
            stu
        )
    except Exception as e:
        print(e)
        return JsonResponse(
            {
                "code":1
            }
        )



@csrf_exempt
def add_stu_list(request):
    db=connect_db()

    if db is None:
        return JsonResponse(
            {"code":2}
        )
    print("链接数据库成功!")
    try:
        sno=request.POST.get('sno')
        sname = request.POST.get('sname')
        sage = request.POST.get('sage')
        sgender = request.POST.get('sgender')
        sdept = request.POST.get('sdept')
        condb = db.cursor()

        condb.execute("insert into student  values("+'\''+sno+'\','+'\''+sname+'\','+'\''+sgender+'\','+sage+','+'\''+sdept+'\')')
        db.commit()

        print("执行sql:"+"insert into student  values("+'\''+sno+'\','+'\''+sname+'\','+'\''+sgender+'\','+sage+','+'\''+sdept+'\')'+'\''+sno+'\''+"成功!")
        return JsonResponse(
        {
                "code":0
            }
        )
    except Exception as e:
        print(e)
        return JsonResponse(
            {
                "code":1
            }
        )


@csrf_exempt
def delete_stu_list(request):
    db=connect_db()

    if db is None:
        return JsonResponse(
            {"code":2}
        )
    print("链接数据库成功!")
    try:
        sno=request.POST.get('sno')
        condb = db.cursor()

        condb.execute("delete from  student where sno="+'\''+sno+'\'')
        db.commit()

        print("执行sql:"+"delete from  student where sno="+'\''+sno+'\''+"成功!")

    except Exception as e:
        print(e)
        return JsonResponse(
            {
                "code":1
            }
        )
    return JsonResponse(
        {
                "code":0
            }
        )

@csrf_exempt
def get_stu_list(request):
    db=connect_db()
    if db is None:
        return JsonResponse(
            {"code":2}
        )

    condb = db.cursor()
    try:
        condb.execute("select * from student");
    except:
        return JsonResponse(
            {"code": 2}
        )
    result=condb.fetchall()

    if len(result)<1:
        return JsonResponse(
            {"code":2}
        )
    stus=[]
    for stu in result:
        stus.append({
            'sno':stu[0],
            'sname':stu[1],
            'sgender':stu[2],
            'sage':stu[3],
            'sdept':stu[4]
        })
    info_list={
        "code":0,
        "stu_info":stus,
    }
    return  JsonResponse(info_list)
