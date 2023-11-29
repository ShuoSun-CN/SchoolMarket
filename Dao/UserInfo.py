from django.db import models
class UserInfo(models.Model):
    class Meta:
        db_table='user_info'
    id=models.IntegerField(primary_key=True)
    user_id=models.CharField(max_length=20)
    user_name=models.CharField(max_length=20)