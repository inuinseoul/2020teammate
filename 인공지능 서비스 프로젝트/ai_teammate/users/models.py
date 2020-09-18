from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# 유저 테이블
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer")
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=20, null=True)
    phone_num = models.CharField(max_length=20, null=True)
    state = models.IntegerField(default=0)


# 흥미 테이블
class Domain(models.Model):
    foreignkey = models.ForeignKey(
        Customer, related_name="domain", on_delete=models.CASCADE, null=True
    )
    health = models.IntegerField(default=0)
    economy = models.IntegerField(default=0)
    culture_art = models.IntegerField(default=0)
    education = models.IntegerField(default=0)
    society = models.IntegerField(default=0)
    technology = models.IntegerField(default=0)
    domain_sum = models.IntegerField(default=0)


# 프로필(점수) 테이블
class Score(models.Model):
    foreignkey = models.ForeignKey(
        Customer, related_name="score", on_delete=models.CASCADE, null=True
    )
    web = models.IntegerField(default=0)
    design = models.IntegerField(default=0)
    machine_learning = models.IntegerField(default=0)
    statistics = models.IntegerField(default=0)
    deep_learning = models.IntegerField(default=0)
    algorithm = models.IntegerField(default=0)
    nlp = models.IntegerField(default=0)
    data_score = models.IntegerField(default=0)
    modeling_score = models.IntegerField(default=0)
    score_sum = models.IntegerField(default=0)


# 선호역할 테이블
class Role(models.Model):
    foreignkey = models.ForeignKey(
        Customer, related_name="role", on_delete=models.CASCADE, null=True
    )
    analysis_hearts = models.IntegerField(default=0)
    web_hearts = models.IntegerField(default=0)
    design_hearts = models.IntegerField(default=0)
    modeling_hearts = models.IntegerField(default=0)
    role_sum = models.IntegerField(default=0)


# 선호스터디 테이블
class Study(models.Model):
    foreignkey = models.ForeignKey(
        Customer, related_name="study", on_delete=models.CASCADE, null=True
    )
    web_hearts = models.IntegerField(default=0)
    design_hearts = models.IntegerField(default=0)
    machine_learning_hearts = models.IntegerField(default=0)
    statistics_hearts = models.IntegerField(default=0)
    deep_learning_hearts = models.IntegerField(default=0)
    algorithm_hearts = models.IntegerField(default=0)
    nlp_hearts = models.IntegerField(default=0)
    basic_python_hearts = models.IntegerField(default=0)
    data_analysis_hearts = models.IntegerField(default=0)
    voice_recog_hearts = models.IntegerField(default=0)
    computer_vision_hearts = models.IntegerField(default=0)
    rec_system_hearts = models.IntegerField(default=0)
    reinforcement_hearts = models.IntegerField(default=0)
    study_sum = models.IntegerField(default=0)


#알림(팀메이트)
class Message(models.Model):
    sender = models.CharField(max_length=20)  # 보낸사람
    sender_pk = models.IntegerField() # 보낸사람의 customer_pk
    recipient = models.CharField(max_length=20)  # 받을사람
    recipient_pk = models.IntegerField() # 받을사람의 recipient_pk
    contents = models.TextField()#메세지내용
    sentAt = models.DateTimeField(auto_now_add=True)  # 쪽지를보낸시간

    def save(self, **kwargs):
        if not self.id:
            self.sentAt = timezone.now()
        super(Message, self).save(**kwargs)

#알림(스터디그룹)
class Study_Message(models.Model):
    sender = models.CharField(max_length=20)  # 보낸사람
    sender_pk = models.IntegerField() # 보낸사람의 customer_pk
    recipient = models.CharField(max_length=20)  # 받을사람
    recipient_pk = models.IntegerField() # 받을사람의 recipient_pk
    contents = models.TextField()#메세지내용
    sentAt = models.DateTimeField(auto_now_add=True)  # 쪽지를보낸시간

    def save(self, **kwargs):
        if not self.id:
            self.sentAt = timezone.now()
        super(Study_Message, self).save(**kwargs)
    
