from django.shortcuts import render, redirect
from users.models import Customer, Domain, Score, Role
from alarm.models import Message

# 알림 리스트 보기
def alarm_list(request, customer_pk):
    customer = Customer.objects.get(pk=customer_pk)
    message_list_team = Message.objects.filter(kind="team").filter(recipient=customer)
    message_list_study = Message.objects.filter(kind="study").filter(recipient=customer)

    context = {
        "message_list_team": message_list_team,
        "message_list_study": message_list_study,
    }

    return render(request, "alarm/alarm_list.html", context)


# 알림삭제(팀메이트)
def del_alarm(request, message_pk):
    message = Message.objects.get(pk=message_pk)
    customer = message.recipient
    message.delete()

    message_list_team = Message.objects.filter(kind="team").filter(recipient=customer)
    message_list_study = Message.objects.filter(kind="study").filter(recipient=customer)

    context = {
        "message_list_team": message_list_team,
        "message_list_study": message_list_study,
    }

    return render(request, "alarm/alarm_list.html", context)


# 팀원제의 받은사람이 팀원제의한 사람의 정보를 볼수있게
def check_info(request, message_pk):
    message = Message.objects.get(pk=message_pk)
    customer = Customer.objects.get(name=message.sender)
    domain = Domain.objects.get(foreignkey=customer)
    score = Score.objects.get(foreignkey=customer)
    role = Role.objects.get(foreignkey=customer)

    context = {
        "customer": customer,
        "domain": domain,
        "score": score,
        "role": role,
    }

    return render(request, "alarm/check_info.html", context)
