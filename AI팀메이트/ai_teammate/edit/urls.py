from django.urls import path
from . import views

app_name = "edit"
urlpatterns = [
    path("info_edit/<int:customer_pk>", views.info_edit, name="info_edit"),  # 정보수정하기
    path(
        "domain_edit/<int:customer_pk>", views.domain_edit, name="domain_edit"
    ),  # 흥미 설문조사 정보수정
    path(
        "score_edit/<int:customer_pk>", views.score_edit, name="score_edit"
    ),  # 실력 설문조사 정보수정
    path(
        "role_edit/<int:customer_pk>", views.role_edit, name="role_edit"
    ),  # 흥미 설문조사 정보수정
    path(
        "study_edit/<int:customer_pk>", views.study_edit, name="study_edit"
    ),  # 흥미 설문조사 정보수정
]