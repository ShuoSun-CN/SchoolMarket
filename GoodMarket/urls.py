from django.urls import path
from GoodMarket import MarketGood,MarketGoodDetail,Cart
gm_urlpattrens=[
   path('getMarketGood/',MarketGood.getMarketGood),
   path('MarketGoodDetail/',MarketGoodDetail.MarketGoodDetail),
path('getMarketGoodDetail/',MarketGoodDetail.getMarketGoodDetail),
   path('addDateGood2Cart/',Cart.addDateGood2Cart),
   path('getCartGood/',Cart.getCartGood),
]
