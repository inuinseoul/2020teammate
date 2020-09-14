from django.urls import path
from . import views

app_name = "edit"
urlpatterns = [
    path('info_edit/<int:customer_pk>', views.info_edit, name='info_edit'),#정보수정하기
    path('survey_edit/<int:customer_pk>', views.survey_edit, name='survey_edit')#설문조사정보수정하기   
]