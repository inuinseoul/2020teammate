from django.shortcuts import render, redirect
from users.models import Customer, Domain, Score, Role, Message, Study_Message

# 알림 리스트 보기
def alarm_list(request, customer_pk):

    message_list_team = Message.objects.all()
    message_list_study = Study_Message.objects.all()
    message_list = []
    message_list2 = []
    for m in message_list_team:
        if m.recipient_pk == customer_pk:
            message_list.append(m)
    for m in message_list_study:
        if m.recipient_pk == customer_pk:
            message_list2.append(m)

    context = {"message_list": message_list, "message_list2": message_list2}

    return render(request, "alarm/alarm_list.html", context)


# 알림생성(팀메이트)
def alarm_create(request, customer_pk):
    customer = Customer.objects.get(pk=customer_pk)
    sender = request.user  # 알림보내는 사람

    Message.objects.create(
        sender_foreignKey=sender.customer,
        sender=sender.customer.name,
        sender_pk=sender.customer.pk,
        recipient_foreignKey=customer,
        recipient=customer.name,
        recipient_pk=customer_pk,
        contents=request.POST["contents"],
    )

    return redirect("home")


# 알림생성(스터디그룹)
def alarm_create2(request, customer_pk):
    customer = Customer.objects.get(pk=customer_pk)
    sender = request.user  # 알림보내는 사람

    Study_Message.objects.create(
        sender_foreignKey=sender.customer,
        sender=sender.customer.name,
        sender_pk=sender.customer.pk,
        recipient_foreignKey=customer,
        recipient=customer.name,
        recipient_pk=customer_pk,
        contents=request.POST["contents"],
    )

    return redirect("home")


# 알림삭제(팀메이트)
def del_alarm(request, message_pk):
    message = Message.objects.get(pk=message_pk)
    customer_pk = message.recipient_pk
    message.delete()

    message_list_team = Message.objects.all()
    message_list_study = Study_Message.objects.all()
    message_list = []
    message_list2 = []
    for m in message_list_team:
        if m.recipient_pk == customer_pk:
            message_list.append(m)
    for m in message_list_study:
        if m.recipient_pk == customer_pk:
            message_list2.append(m)

    context = {"message_list": message_list, "message_list2": message_list2}

    return render(request, "alarm/alarm_list.html", context)


# 알림삭제(스터디그룹)
def del_alarm2(request, message_pk):
    message2 = Study_Message.objects.get(pk=message_pk)
    customer_pk = message2.recipient_pk
    message2.delete()

    message_list_team = Message.objects.all()
    message_list_study = Study_Message.objects.all()
    message_list = []
    message_list2 = []
    for m in message_list_team:
        if m.recipient_pk == customer_pk:
            message_list.append(m)
    for m in message_list_study:
        if m.recipient_pk == customer_pk:
            message_list2.append(m)

    context = {"message_list": message_list, "message_list2": message_list2}

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


# 팀원제의 받은사람이 팀원제의한 사람의 정보를 볼수있게
def check_info2(request, message_pk):
    message = Study_Message.objects.get(pk=message_pk)
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
