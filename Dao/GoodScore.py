from django.db import models
class GoodScore(models.Model):
    class Meta:
        db_table='good_score'
    good_id=models.CharField(max_length=20)
    score=models.IntegerField()
    score_id=models.CharField(max_length=20)
    score_dscp=models.CharField(max_length=255)
