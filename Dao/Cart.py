from django.db import models
class Cart(models.Model):
    class Meta:
        db_table='cart'
        unique_together=("good_id","stu_id")
    good_id=models.CharField(max_length=20,primary_key=True)
    stu_id=models.CharField(max_length=20)
    num=models.IntegerField()
    add_time=models.DateTimeField()
