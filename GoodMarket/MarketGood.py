import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Dao.Good import Good
from Dao.Cart import Cart
@csrf_exempt
def getMarketGood(req):
    try:
        good_list=list(Good.objects.get_queryset().values_list())
        cart_num=Cart.objects.filter().__len__()
        good_list_back=[]
        print(good_list)
        for good in good_list:
            good_temp={
                'good_id':good[0],
                'good_name':good[1],
                'good_price':good[2],
                'main_image':'/good_image/'+good[5],
            }

            good_list_back.append(good_temp)
        good_dict={"code":0,"good_list":good_list_back,'cart_num':cart_num}
        print(good_dict)
        return JsonResponse(good_dict)
    except Exception as e:
        print(e)
        return None