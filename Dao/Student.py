from django.db import models
class UserAccount(models.Model):
    class Meta:
        db_table='student'
    sname=models.CharField(max_length=20)
    sno=models.CharField(max_length=20,primary_key=True)
