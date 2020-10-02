from django.shortcuts import render
from users.models import Domain
from alarm.models import Message
from django.http import StreamingHttpResponse
import cv2
import numpy as np
import threading

# Create your views here.
def home(request):
    max_domain = -1
    user = request.user
    context = {}
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

        customer = user.customer
        team_message_list = Message.objects.filter(kind="team").filter(
            recipient=customer
        )
        study_message_list = Message.objects.filter(kind="study").filter(
            recipient=customer
        )

        context = {
            "team_message_list": team_message_list,
            "study_message_list": study_message_list,
            "max_domain": max_domain,
        }

    return render(request, "home/home.html", context)
