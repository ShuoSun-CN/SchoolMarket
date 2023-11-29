from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Dao.Good import Good
from Dao.Cart import Cart

from django.shortcuts import render
@csrf_exempt
def MarketGoodDetail(req):
    return render(req,"market_good_detail.html")

@csrf_exempt
def getMarketGoodDetail(req):
    try:
        good_id=req.POST.get("good_id")
        good=Good.objects.filter(good_id=good_id)[0]
        cart_num = Cart.objects.filter().__len__()


        good_dict={
            "code":0,
            'good_id':good.good_id,
            'good_name':good.good_name,
            'good_price':good.price,
            'num':good.num,
            'main_image':'/good_image/'+good.main_image,
            'cart_num':cart_num


        }


        print(good_dict)
        return JsonResponse(good_dict)
    except Exception as e:
        print(e)
        return JsonResponse({
            "code":1
        })