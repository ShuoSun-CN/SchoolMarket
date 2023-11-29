
import psycopg2
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from login.utils.email_verify import verifyEmail
from Dao.UserAccount import UserAccount
from Dao.UserInfo import UserInfo
@csrf_exempt
def verify_login(request):
    user_id = request.POST.get("user_id")
    password_get = request.POST.get("password")
    try:
        password_true=UserAccount.objects.filter(user_id=user_id)[0].user_password
    except:
        return JsonResponse(
            {"code":1}
        )
    if password_true==password_get:
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
    try:
        user_id=req.COOKIES['user_verify']
        user_name=UserInfo.objects.filter(user_id=user_id)[0].user_name
        print(user_name)
        return JsonResponse({
            "code":0,
            "sname":user_name
        })
    except Exception as e:
        print(e)
        response=JsonResponse(
            {
                'code':1
            }
        )
        response.delete_cookie('user_verify')
        return  response
email_code=""

@csrf_exempt
def send_register_code(req):
    global email_code
    email_code=True
    email_address=req.POST.get("email")
    email_code=verifyEmail(email_address)
    if not email_code:
        return JsonResponse({
            "code":1
        })
    else:
        return JsonResponse({
            "code":0
        })

@csrf_exempt
def verify_register(request):
    db=connect_db()
    if db is None:
        return JsonResponse(
            {"code":2}
        )
    condb=db.cursor()
    user_id=request.POST.get("user_id")
    password=request.POST.get("user_password")
    sno=request.POST.get("sno")
    email_code_get=request.POST.get("email_code")
    if email_code_get==email_code:
        print("yes")
        try:
            condb.execute("insert into login_users(user_id,user_password,sno,email) values("+'\''+user_id+'\','+'\''+password+'\',\''+sno+'\')');
            db.commit()
            return JsonResponse({
                "code":0
            })
        except:
            return JsonResponse({
                "code":1
            })

    else:
        return JsonResponse({
            "code":2
        })