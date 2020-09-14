from django.shortcuts import render,redirect
from users.models import Customer, Domain, Score, Role, Message

#알리미
def alarm_list(request, customer_pk):
    if request.method == 'POST':
        customer = Customer.objects.get(pk=customer_pk)
        sender = request.user

        Message.objects.create(
                            sender = sender.customer.name,
                            recipient = customer.name,
                        )

        return redirect('home')
    
    message_list = Message.objects.all()

    context = {'message_list' : message_list}

    return render(request, 'alarm/alarm_list.html', context)

#알림삭제
def del_alarm(request, message_pk):
    message = Message.objects.get(pk=message_pk)
    message.delete()
    message_list = Message.objects.all()

    context = {'message_list' : message_list}

    return render(request, 'alarm/alarm_list.html',context)

#팀원제의 받은사람이 팀원제의한 사람의 정보를 볼수있게
def check_info(request, message_pk):
    message = Message.objects.get(pk=message_pk)
    customer = Customer.objects.get(name=message.sender)
    domain = Domain.objects.get(foreignkey=customer)
    score = Score.objects.get(foreignkey=customer)
    role = Role.objects.get(foreignkey=customer)

    context = {'customer' : customer, 'domain' : domain, 'score' : score, 'role' : role,}

    return render(request, 'alarm/check_info.html', context)