from django.urls import path
from . import views

app_name = "team_rec"
urlpatterns = [
    # path("choice", views.choice, name="choice"),
    # path("team_rec_list/<int:customer_pk>", views.team_rec_list, name="team_rec_list"),
    path("person/<int:customer_pk>", views.team_rec_list, name="person"),
]
