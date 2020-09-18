from django.urls import path
from . import views

app_name = "alarm"
urlpatterns = [
    path('alarm_list/<int:customer_pk>', views.alarm_list, name='alarm_list'),
    path('alarm_create/<int:customer_pk>', views.alarm_create, name='alarm_create'),
    path('del_alarm/<int:message_pk>', views.del_alarm, name='del_alarm'),
    path('check_info/<int:message_pk>', views.check_info, name='check_info'),
    path('alarm_create2/<int:customer_pk>', views.alarm_create2, name='alarm_create2'),
    path('del_alarm2/<int:message_pk>', views.del_alarm2, name='del_alarm2'),
    path('check_info2/<int:message_pk>', views.check_info2, name='check_info2'), 
]