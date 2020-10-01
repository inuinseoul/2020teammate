from django.http import request
from django.shortcuts import render
from django.contrib import auth
from sklearn.metrics.pairwise import cosine_similarity
from django_pandas.io import read_frame
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from team_rec.forms import Team_form
from django.utils import timezone
from django.shortcuts import redirect

from users.models import Customer, Domain, Score, Role, Message
from team_rec.models import Team_list

# font_name = font_manager.FontProperties(
#     fname="/static/malgun.ttf"
# ).get_name()
# rc("font", family=font_name)
def choice(request):
    return render(request, "team_rec/team_choice.html")

# 팀메이트 추천시스템
def team_rec_list(request, customer_pk):
    page = 5
    if request.method == "POST":
        if request.POST["request"] != "0":
            page = int(request.POST["page"])
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

    grade_subs = np.abs(customer_score_sum - customer_score_sum[my_num]) * 0.001
    evaluation_value = (
        score_similarity[my_num]
        + grade_subs
        - domain_similarity[my_num]
        + role_similarity[my_num]
    )
    recommend_id_list = evaluation_value.sort_values().index.tolist()

    if my_num in recommend_id_list:
        recommend_id_list.remove(my_num)
    recommend_pk_list = df0.iloc[recommend_id_list].id
    recommend_customer_list = []
    recommend_customer_list_already = []
    recommend_customer_length = len(recommend_pk_list)

    for i in recommend_pk_list:
        now_customer = Customer.objects.get(pk=int(i))
        if now_customer.team_state == 1:
            recommend_customer_list_already.append(now_customer)
        else:
            recommend_customer_list.append(now_customer)

    recommend_customer_list = recommend_customer_list + recommend_customer_list_already

    if len(recommend_customer_list) <= 5:
        recommend_customer_list = recommend_customer_list
    elif len(recommend_customer_list) <= page:
        recommend_customer_list = recommend_customer_list[page - 5 :]
    else:
        recommend_customer_list = recommend_customer_list[page - 5 : page]

    for now_customer in recommend_customer_list:
        i = now_customer.pk
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

    context = {
        "recommend_customer_list": recommend_customer_list,
        "page": page,
        "recommend_customer_length": recommend_customer_length,
    }
    return render(request, "team_rec/team_rec_list.html", context)


def team(request):
    # page = 10
    # if request.method == "POST":
    #     page = int(request.POST["page"]) + 10

    team_list = Team_list.objects.all()
    df0 = read_frame(team_list)

    team_data = df0.loc[
        :,
        [
            "leader",
            "name",
            "intro",
            "state",
            "created_date",
        ],
    ]

    all_list = []
    for i in range(team_data.shape[0]):
        all_list.append(
            {
                "leader": team_data["leader"][i],
                "name": team_data["name"][i],
                "intro": team_data["intro"][i],
                "state": team_data["state"][i],
                "created_date": team_data["created_date"][i],
            }
        )

# all_list = []
# if team_data.shape[0] < page:
#     for i in range(page - team_data.shape[0]):
#         all_list.append(
#             {
#                 "leader": team_data["leader"][page + i - 10],
#                 "name": team_data["name"][page + i - 10],
#                 "intro": team_data["intro"][page + i - 10],
#                 "state": team_data["state"][page + i - 10],
#                 "created_date": team_data["created_date"][page + i - 10],
#             }
#         )
# else:
#     for i in range(10):
#         all_list.append(
#             {
#                 "leader": team_data["leader"][page + i - 10],
#                 "name": team_data["name"][page + i - 10],
#                 "intro": team_data["intro"][page + i - 10],
#                 "state": team_data["state"][page + i - 10],
#                 "created_date": team_data["created_date"][page + i - 10],
#             }
#         )
# context = {"all_list": all_list, "page": page, "team_num": team_data.shape[0]}

    context = {"all_list": all_list}    

    return render(request, "team_rec/team_team.html",context)

def member(request):
    return render(request, "team_rec/team_member.html")

def team_make(request):
    if request.method == "POST":
        form = Team_form(request.POST)
        if form.is_valid():
            Team_list = form.save(commit=False)
            Team_list.leader = request.user
            Team_list.created_date = timezone.now()
            Team_list.save()
            return redirect('/team_rec/team/')#, pk=post.pk)

    else:
        form = Team_form()
    return render(request, "team_rec/team_make.html",{'form': form})


def team_edit(request):
    if request.method == "POST":
        form = Team_form(request.POST)
        if form.is_valid():
            Team_list = form.save(commit=False)
            Team_list.leader = request.user
            Team_list.created_date = timezone.now()
            Team_list.save()
            # return redirect('team_edit', pk=post.pk)

    else:
        form = Team_form()
    return render(request, "team_rec/team_make.html",{'form': form})