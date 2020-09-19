from django.shortcuts import render
from users.models import Message, Study_Message, Domain

# Create your views here.
def home(request):
    max_domain = -1
    user = request.user
    if user.is_authenticated:
        my_domain = Domain.objects.get(foreignkey=user.customer)
        domains = [
            my_domain.health,
            my_domain.economy,
            my_domain.culture_art,
            my_domain.education,
            my_domain.society,
            my_domain.technology,
        ]
        max_value = -1
        max_index = -1
        for i in range(6):
            if int(domains[i]) > max_value:
                max_value = int(domains[i])
                max_index = i
        domain_names = [
            "health",
            "economy",
            "culture_art",
            "education",
            "society",
            "technology",
        ]
        max_domain = max_index

    message_list = Message.objects.all()
    study_message_list = Study_Message.objects.all()

    message_pk = []
    for i in message_list:
        if i.recipient_pk not in message_pk:
            message_pk.append(i.recipient_pk)

    study_pk = []
    for j in study_message_list:
        if j.recipient_pk not in study_pk:
            study_pk.append(j.recipient_pk)

    context = {"message_pk": message_pk, "study_pk": study_pk, "max_domain": max_domain}

    return render(request, "home/home.html", context)
