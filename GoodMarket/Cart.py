import json
import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Dao.Good import Good
from Dao.Cart import Cart
@csrf_exempt
def addDateGood2Cart(req):
    try:
        good_id=req.POST.get("good_id")
        good_num=req.POST.get("good_num")
        user_id = req.COOKIES['user_verify']



        cart=Cart(stu_id=user_id,good_id=good_id,num=good_num,add_time=datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S"))
        cart.save()
        cart_num = Cart.objects.filter().__len__()
        return JsonResponse({
            "cart_num":cart_num,
            "code":0
        })
    except Exception as e:
        print(e)
        return JsonResponse({
            "code":1
        })
@csrf_exempt
def getCartGood(req):
    user_id=req.COOKIES['user_verify']
    try:
        good_list=list(Cart.objects.get_queryset().values_list())
        cart_num=Cart.objects.filter(stu_id=user_id).__len__()
        good_list_back=[]
        print(good_list)
        for good_cart in good_list:
            good = Good.objects.filter(good_id=good_cart[0])[0]
            good_temp={
                'good_name':good.good_name,
                'good_price':good.price,
                'main_image':'/good_image/'+good.main_image,
                'num':good_cart[2]
            }
            good_list_back.append(good_temp)
        good_dict={"code":0,"good_list":good_list_back}
        print(good_dict)
        return JsonResponse(good_dict)
    except Exception as e:
        print(e)
        return None