from django.urls import path
from . import views

app_name = "team_rec"
urlpatterns = [
    path('team_rec_list/<int:customer_pk>', views.team_rec_list, name='team_rec_list'),
    path('t_check_info/<int:customer_pk>', views.t_check_info, name='t_check_info')
]