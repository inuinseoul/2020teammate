import csv
import os
import django
import sys

os.chdir('.')
print("Current dir=", end=""), print(os.getcwd())
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR=", end=""), print(BASE_DIR)

sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ai_teammate.settings")	# 1. 여기서 프로젝트명.settings입력
django.setup()

# 위의 과정까지가 python manage.py shell을 키는 것과 비슷한 효과
###########################################################################################

# 1. User 데이터 업로드
import csv
from django.contrib.auth.models import User
with open('users/user.csv', encoding='UTF-8') as csv_file:
    data_reader = csv.reader(csv_file)
    next(data_reader, None)
    data = []
    for username, password, *__ in data_reader:
        user = User(username=username)
        user.set_password(password)
        data.append(user)
    User.objects.bulk_create(data)

# 2. customer 데이터 업로드

CSV_PATH = 'users/customer.csv'	# 3. csv 파일 경로
import csv
from users.models import Customer	# 2. App이름.models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

bulk_list = []
with open(CSV_PATH, encoding='UTF-8') as csvfile:	# 4. newline =''
    data_reader = csv.reader(csvfile)
    next(data_reader, None)
    for row in data_reader:
        bulk_list.append(Customer(		# 5. class명.objects.create
            user = User.objects.get(username= row[0]),
            name = row[1],
            email = row[2],
            phone_num = row[3],
            team_state = row[4],
            study_state = row[5],
            intro = row[6],
        ))

Customer.objects.bulk_create(bulk_list)

# 3. Domain 데이터 업로드

CSV_PATH = 'users/domain.csv'	# 3. csv 파일 경로
# CSV_PATH = 'C:/Users/leeso/OneDrive/바탕 화면/data/domain_index.csv'
import csv
from users.models import Domain,Customer	# 2. App이름.models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

bulk_list = []
with open(CSV_PATH, encoding='UTF-8') as csvfile:	# 4. newline =''
    data_reader = csv.reader(csvfile)
    next(data_reader, None)
    for row in data_reader:
        bulk_list.append(Domain(		# 5. class명.objects.create
            foreignkey = Customer.objects.get(name= row[0]),
            health = row[1],
            economy = row[2],
            culture_art = row[3],
            education = row[4],
            society = row[5],
            technology = row[6],
            domain_sum = row[7],
        ))

Domain.objects.bulk_create(bulk_list)
Domain.objects.values()

# 4. Message 데이터 업로드
# 5. Roles 데이터 업로드

CSV_PATH = 'users/role.csv'	# 3. csv 파일 경로
# CSV_PATH = 'C:/Users/leeso/OneDrive/바탕 화면/data/domain_index.csv'
import csv
from users.models import Role,Customer	# 2. App이름.models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

bulk_list = []
with open(CSV_PATH, encoding='UTF-8') as csvfile:	# 4. newline =''
    data_reader = csv.reader(csvfile)
    next(data_reader, None)
    for row in data_reader:
        bulk_list.append(Role(		# 5. class명.objects.create
            foreignkey = Customer.objects.get(name= row[0]),
            analysis_hearts = row[1],
            web_hearts = row[2],
            design_hearts = row[3],
            modeling_hearts = row[4],
            role_sum = row[5],
        ))

Role.objects.bulk_create(bulk_list)
Role.objects.values()

# 6. Score 데이터 업로드
# class Score(models.Model):
#     foreignkey = models.ForeignKey(
#         Customer, related_name="score", on_delete=models.CASCADE, null=True
#     )
#     web = models.IntegerField(default=0)
#     design = models.IntegerField(default=0)
#     machine_learning = models.IntegerField(default=0)
#     statistics = models.IntegerField(default=0)
#     deep_learning = models.IntegerField(default=0)
#     algorithm = models.IntegerField(default=0)
#     nlp = models.IntegerField(default=0)
#     data_score = models.IntegerField(default=0)
#     modeling_score = models.IntegerField(default=0)
#     score_sum = models.IntegerField(default=0)

CSV_PATH = 'users/score.csv'	# 3. csv 파일 경로
# # CSV_PATH = 'C:/Users/leeso/OneDrive/바탕 화면/data/domain_index.csv'
import csv
from users.models import Score,Customer	# 2. App이름.models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

bulk_list = []
with open(CSV_PATH, encoding='UTF-8') as csvfile:	# 4. newline =''
    data_reader = csv.reader(csvfile)
    next(data_reader, None)
    for row in data_reader:
        bulk_list.append(Score(		# 5. class명.objects.create
            foreignkey = Customer.objects.get(name= row[0]),
            web = row[1],
            design = row[2],
            machine_learning = row[3],
            statistics = row[4],
            deep_learning = row[5],
            algorithm = row[6],
            nlp = row[7],
            data_score = row[8],
            modeling_score = row[9],
            score_sum = row[10],
        ))

Score.objects.bulk_create(bulk_list)
Score.objects.values()

# 7. Study_message 데이터 업로드
# 8. Study 데이터 업로드

CSV_PATH = 'users/study.csv'	# 3. csv 파일 경로
# CSV_PATH = 'C:/Users/leeso/OneDrive/바탕 화면/data/domain_index.csv'
import csv
from users.models import Study,Customer	# 2. App이름.models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

bulk_list = []
with open(CSV_PATH, encoding='UTF-8') as csvfile:	# 4. newline =''
    data_reader = csv.reader(csvfile)
    next(data_reader, None)
    for row in data_reader:
        bulk_list.append(Study(		# 5. class명.objects.create
            foreignkey = Customer.objects.get(name= row[0]),
            web_hearts = row[1],
            design_hearts = row[2],
            machine_learning_hearts = row[3],
            statistics_hearts = row[4],
            deep_learning_hearts = row[5],
            algorithm_hearts = row[6],
            nlp_hearts = row[7],
            basic_python_hearts = row[8],
            data_analysis_hearts = row[9],
            voice_recog_hearts = row[10],
            computer_vision_hearts = row[11],
            rec_system_hearts = row[12],
            reinforcement_hearts = row[13],
            study_sum = row[14],
        ))

Study.objects.bulk_create(bulk_list)
Study.objects.values()


# 9. newsletter 데이터 업로드
CSV_PATH = 'newsletter/result_0919.csv'	# 3. csv 파일 경로
# import csv
from newsletter.models import *	# 2. App이름.models

bulk_list = []
with open(CSV_PATH, encoding='UTF-8') as csvfile:	# 4. newline =''
    data_reader = csv.reader(csvfile)
    next(data_reader, None)
    for row in data_reader:
        bulk_list.append(News(		# 5. class명.objects.create
            link = row[0],
            title = row[1],
            date = row[2],
            content = row[3],
            tag = row[4],
            big_category = row[5],
            category = row[6],
            team_category = row[7]
        ))

News.objects.bulk_create(bulk_list)
# News.objects.values()

# Customer.objects.bulk_create(bulk_list)
# Customer.objects.values()

print('Okay')