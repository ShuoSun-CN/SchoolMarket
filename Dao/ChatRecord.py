from django.db import models
class ChatRecord(models.Model):
    class Meta:
        db_table="chat_record"
    id=models.IntegerField(primary_key=True)
    sender_id=models.CharField(max_length=20)
    receiver_id=models.CharField(max_length=20)
    send_time=models.DateTimeField()