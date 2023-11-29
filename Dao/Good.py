from django.db import models
class Good(models.Model):
    class Meta:
        db_table='good'
    good_id=models.CharField(max_length=20,primary_key=True)
    good_name=models.CharField(max_length=20)
    price=models.FloatField()
    num=models.IntegerField(max_length=20)
    stu_id=models.CharField(max_length=20)
    main_image=models.CharField(max_length=255)
