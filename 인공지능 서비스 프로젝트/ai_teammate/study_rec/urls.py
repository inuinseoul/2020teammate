from django.urls import path
from . import views

app_name = "study_rec"
urlpatterns = [
    path('study_rec_list/<int:customer_pk>', views.study_rec_list, name='study_rec_list'),
    path('s_check_info/<int:customer_pk>', views.s_check_info, name='s_check_info')
]