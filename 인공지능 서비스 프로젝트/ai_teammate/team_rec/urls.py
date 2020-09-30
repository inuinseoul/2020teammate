from django.urls import path
from . import views

app_name = "team_rec"
urlpatterns = [
    path("choice", views.choice, name="choice"),
    path("person/<int:customer_pk>", views.team_rec_list, name="person"),
    path("team/<int:customer_pk>", views.team, name="team"),
    path("member/<int:customer_pk>", views.team, name="member"),
    path("make/<int:customer_pk>", views.make, name="make"),

]
