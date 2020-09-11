from django.db import models
# Create your models here.
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='customer',null=True)
    name = models.CharField(max_length=10)
    class_num = models.IntegerField( null=True)
    #추가해줄게 많다.....

    # 클래스명 + app이름으로 저장할 거면 밑에 사용 x
    # class Meta: #메타 클래스를 이용하여 테이블명 지정
    #     db_table = 'test_user'

class Score(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    web =models.IntegerField()
    design =models.IntegerField()
    machine_learning =models.IntegerField() 
    statistics = models.IntegerField()
    deep_learning =models.IntegerField()
    algorithm =models.IntegerField()
    nlp = models.IntegerField()

class Domain(models.Model):
    user_id= models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    domain_id = models.CharField(max_length=10)
    domain_hearts =models.IntegerField()

class Study_list(models.Model):
    study_name = models.CharField(max_length=10)

class Study(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    study_id = models.ForeignKey(Study_list, on_delete=models.CASCADE, null=True)
    study_hearts = models.IntegerField()

class Role(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    analysis_hearts = models.IntegerField()
    web_hearts = models.IntegerField()
    design_hearts = models.IntegerField()
    modeling_hearts = models.IntegerField()
