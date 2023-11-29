from django.db import models
class DealOrder(models.Model):
    class Meta:
        db_table="deal_order"
    good_id=models.CharField(max_length=20)
    num=models.IntegerField()
    price=models.FloatField()
    order_id=models.CharField(max_length=20,primary_key=True)
    buyer_id=models.CharField(max_length=20)
    create_date=models.DateTimeField()
    order_status=models.IntegerField()
    