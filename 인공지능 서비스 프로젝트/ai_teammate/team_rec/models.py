from django.db import models
# from users.models import Customer
from django.contrib.auth.models import User



# Create your models here.

class Team_make(models.Model) :
    leader = models.ForeignKey(
        User, related_name="leader", on_delete=models.CASCADE, null=True
    ) # 팀장
    name = models.CharField(max_length=20) # 팀명
    intro = models.TextField() # 팀 소개
    state = models.IntegerField(default=0) # 팀상태
    

class Team_member(models.Model) : 
    team_id = models.ForeignKey(
        Team_make, related_name="team_id", on_delete=models.CASCADE, null=True
    )
    member = models.ForeignKey(
    User, related_name="team_member", on_delete=models.CASCADE, null=True
    )
