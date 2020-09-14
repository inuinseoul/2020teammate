from django.shortcuts import render
from users.models import Customer, Domain, Score, Role
from django.contrib import auth
from sklearn.metrics.pairwise import cosine_similarity
from django_pandas.io import read_frame
import numpy as np
import pandas as pd

#팀메이트 추천시스템
def team_rec_list(request,customer_pk):
    customer_list = Customer.objects.all()
    score_list = Score.objects.all()
    domain_list = Domain.objects.all()
    role_list = Role.objects.all()    
    df0 = read_frame(customer_list)
    df1 = read_frame(score_list)
    df2 = read_frame(domain_list)
    df3 = read_frame(role_list)
    customer_score = df1.loc[:,['web', 'design', 'data_score', 'modeling_score']]
    customer_score_sum = customer_score.sum(axis=1)
    customer_domain = df2.loc[:,['health', 'economy', 'culture_art', 'education', 'society', 'technology']]
    customer_role = df3.loc[:,['analysis_hearts', 'web_hearts','design_hearts', 'modeling_hearts']]   

    my_num = df0[df0['user'] == customer_pk].index.tolist()[0]

    # 각 유사도측정
    score_similarity = cosine_similarity(customer_score, customer_score)
    domain_similarity = cosine_similarity(customer_domain, customer_domain)
    role_similarity = cosine_similarity(customer_role, customer_role)

    grade_subs = np.abs(customer_score_sum - customer_score_sum[my_num]) * 0.1
    evaluation_value = score_similarity[my_num-1] + grade_subs - domain_similarity[my_num-1] + role_similarity[my_num-1]
    recommend_id_list = evaluation_value.sort_values().index.tolist()
    if my_num in recommend_id_list:
        recommend_id_list.remove(my_num)
    recommend_pk_list = df0.iloc[recommend_id_list].id

    recommend_customer_list = []
    recommend_customer_score_list = []
    recommend_customer_domain_list = []
    recommend_customer_role_list = []

    for i in recommend_pk_list:
        now_customer = Customer.objects.get(pk=int(i))
        recommend_customer_list.append(now_customer)
        recommend_customer_score_list.append(Score.objects.get(foreignkey=now_customer))
        recommend_customer_domain_list.append(Domain.objects.get(foreignkey=now_customer))
        recommend_customer_role_list.append(Role.objects.get(foreignkey=now_customer))

    context = {
        'recommend_customer_list' : recommend_customer_list,
        'recommend_customer_score_list' : recommend_customer_score_list,
        'recommend_customer_domain_list' : recommend_customer_domain_list,
        'recommend_customer_role_list' : recommend_customer_role_list
    }
    return render(request, 'team_rec/team_rec_list.html', context)

#추천회원 정보보기
def t_check_info(request, customer_pk):
    customer = Customer.objects.get(pk=customer_pk)
    domain = Domain.objects.get(foreignkey=customer)
    score = Score.objects.get(foreignkey=customer)
    role = Role.objects.get(foreignkey=customer)

    context = {'customer' : customer, 'domain' : domain, 'score' : score, 'role' : role}

    return render(request, 'team_rec/t_check_info.html', context)