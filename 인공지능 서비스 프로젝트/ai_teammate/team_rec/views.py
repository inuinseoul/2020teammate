from django.http import request
from django.shortcuts import render
from users.models import Customer, Domain, Score, Role, Message
from django.contrib import auth
from sklearn.metrics.pairwise import cosine_similarity
from django_pandas.io import read_frame
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc("font", family=font_name)

# 팀메이트 추천시스템
def team_rec_list(request, customer_pk):
    page = 5
    if request.method == "POST":
        if request.POST["request"] != "0":
            page = request.POST["page"]
            to_pk = request.POST["request"]
            customer = Customer.objects.get(pk=to_pk)
            sender = request.user  # 알림보내는 사람

            Message.objects.create(
                sender_foreignKey=sender.customer,
                sender=sender.customer.name,
                sender_pk=sender.customer.pk,
                recipient_foreignKey=customer,
                recipient=customer.name,
                recipient_pk=to_pk,
                contents=request.POST["contents"],
            )
        if request.POST["request"] == "0":
            page = int(request.POST["page"]) + 5

    customer_list = Customer.objects.all()
    score_list = Score.objects.all()
    domain_list = Domain.objects.all()
    role_list = Role.objects.all()
    df0 = read_frame(customer_list)
    df1 = read_frame(score_list)
    df2 = read_frame(domain_list)
    df3 = read_frame(role_list)
    customer_score = df1.loc[:, ["web", "design", "data_score", "modeling_score"]]
    customer_score_sum = customer_score.sum(axis=1)
    customer_domain = df2.loc[
        :, ["health", "economy", "culture_art", "education", "society", "technology"]
    ]
    customer_role = df3.loc[
        :, ["analysis_hearts", "web_hearts", "design_hearts", "modeling_hearts"]
    ]

    my_num = df0[df0["user"] == customer_pk].index.tolist()[0]

    # 각 유사도측정
    score_similarity = cosine_similarity(customer_score, customer_score)
    domain_similarity = cosine_similarity(customer_domain, customer_domain)
    role_similarity = cosine_similarity(customer_role, customer_role)

    grade_subs = np.abs(customer_score_sum - customer_score_sum[my_num]) * 0.1
    evaluation_value = (
        score_similarity[my_num - 1]
        + grade_subs
        - domain_similarity[my_num - 1]
        + role_similarity[my_num - 1]
    )
    recommend_id_list = evaluation_value.sort_values().index.tolist()
    if my_num in recommend_id_list:
        recommend_id_list.remove(my_num)
    recommend_pk_list = df0.iloc[recommend_id_list].id

    recommend_customer_list = []
    recommend_customer_list_already = []
    recommend_customer_length = len(recommend_pk_list)
    if len(recommend_pk_list) <= 5:
        recommend_pk_list = recommend_pk_list
    elif len(recommend_pk_list) <= page:
        recommend_pk_list = recommend_pk_list[page - 5 :]
    else:
        recommend_pk_list = recommend_pk_list[page - 5 : page]

    for i in recommend_pk_list:
        now_customer = Customer.objects.get(pk=int(i))
        if now_customer.team_state == 1:
            recommend_customer_list_already.append(now_customer)
        else:
            recommend_customer_list.append(now_customer)
        domain_index = [
            "건강",
            "경제",
            "문화",
            "교육",
            "사회",
            "기술",
        ]
        domain_values = [
            Domain.objects.get(foreignkey=now_customer).health,
            Domain.objects.get(foreignkey=now_customer).economy,
            Domain.objects.get(foreignkey=now_customer).culture_art,
            Domain.objects.get(foreignkey=now_customer).education,
            Domain.objects.get(foreignkey=now_customer).society,
            Domain.objects.get(foreignkey=now_customer).technology,
        ]
        plt.figure(figsize=(3, 3))
        plt.bar(
            domain_index,
            domain_values,
            color=["#F7BE81", "#F5DA81", "#F3F781", "#D8F781", "#9FF781", "#81F79F"],
        )
        plt.savefig(f"./static/domain_graph_{i}.png")

        role_index = ["데이터", "웹", "디자인", "모델링"]
        role_values = [
            Role.objects.get(foreignkey=now_customer).analysis_hearts,
            Role.objects.get(foreignkey=now_customer).web_hearts,
            Role.objects.get(foreignkey=now_customer).design_hearts,
            Role.objects.get(foreignkey=now_customer).modeling_hearts,
        ]
        plt.figure(figsize=(3, 3))
        plt.bar(
            role_index,
            role_values,
            color=["#F78181", "#A9E2F3", "#D0A9F5", "#F5A9F2"],
        )
        plt.savefig(f"./static/role_graph_{i}.png")
    recommend_customer_list = recommend_customer_list + recommend_customer_list_already
    context = {
        "recommend_customer_list": recommend_customer_list,
        "page": page,
        "recommend_customer_length": recommend_customer_length,
    }
    return render(request, "team_rec/team_rec_list.html", context)
