from django.shortcuts import render
from users.models import Message, Study_Message

# Create your views here.
def home(request):
    message_list = Message.objects.all()
    study_message_list = Study_Message.objects.all()
    
    message_pk =[]
    for i in message_list:
        if i.recipient_pk not in message_pk:
            message_pk.append(i.recipient_pk)

    study_pk = []
    for j in study_message_list:
        if j.recipient_pk not in study_pk:
            study_pk.append(j.recipient_pk) 

    context = {'message_pk':message_pk, 'study_pk':study_pk}

    return render(request, 'home/home.html',context)
    