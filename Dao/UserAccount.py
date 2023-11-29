from django.db import models
class UserAccount(models.Model):
    class Meta:

        db_table='user_account'
    user_id=models.CharField(primary_key=True,max_length=20)
    user_password=models.CharField(max_length=20)
    sno=models.CharField(max_length=20)
    email=models.CharField(max_length=40)
    priority=models.IntegerField()