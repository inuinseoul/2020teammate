from django.db import models
from users.models import Customer

# Create your models here.
# 알림(팀메이트)
class Message(models.Model):
    sender = models.ForeignKey(
        Customer, related_name="send_message", on_delete=models.CASCADE, null=True
    )
    recipient = models.ForeignKey(
        Customer, related_name="received_message", on_delete=models.CASCADE, null=True
    )
    contents = models.TextField()  # 메세지내용
    sentAt = models.DateTimeField(auto_now_add=True)  # 쪽지를보낸시간
    kind = models.CharField(max_length=10)
