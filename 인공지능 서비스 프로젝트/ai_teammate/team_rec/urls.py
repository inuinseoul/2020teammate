from django.urls import path
from . import views

app_name = "team_rec"
urlpatterns = [
    path("choice", views.choice, name="choice"),
    path("person/<int:customer_pk>", views.team_rec_list, name="person"),
    path("team/", views.team, name="team"),
    path("member/<int:customer_pk>", views.member, name="member"),
    path("make/", views.team_make, name="team_make"),
]
