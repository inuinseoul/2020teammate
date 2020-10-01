from django.db import models
# from users.models import Customer
from django.contrib.auth.models import User
from django.utils import timezone



# Create your models here.

class Team_list(models.Model) :
    leader = models.ForeignKey(
        User, related_name="leader", on_delete=models.CASCADE, null=True
    ) # 팀장
    name = models.CharField(max_length=20) # 팀명 - 입력 받음
    intro = models.TextField() # 팀 소개 - 입력 받음
    state = models.IntegerField(default=0) # 팀상태
    created_date = models.DateTimeField(default=timezone.now)
    

class Team_member(models.Model) : 
    team_id = models.ForeignKey(
        Team_list, related_name="team_id", on_delete=models.CASCADE, null=True
    )
    member = models.ForeignKey(
    User, related_name="team_member", on_delete=models.CASCADE, null=True
    )
