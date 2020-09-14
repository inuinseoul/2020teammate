"""team_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from team_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #홈
    path('', views.home, name='home'),

    #회원가입&로그인
    path('signup/', views.signup, name='signup'),
    path('signup2/<int:customer_pk>', views.signup2, name='signup2'),
    path('signup3/<int:customer_pk>', views.signup3, name='signup3'),
    path('signup4/<int:customer_pk>', views.signup4, name='signup4'),
    path('signup5/<int:customer_pk>', views.signup5, name='signup5'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    #팀추천,스터디그룹추천,추천시스템사용자정보
    path('rec/<int:customer_pk>', views.rec, name='rec'),
    path('grp/<int:customer_pk>', views.grp, name='grp'),
    path('rec_customer/<int:customer_pk>', views.rec_customer, name='rec_customer'),

    #정보수정,설문조사정보수정
    path('edit/<int:customer_pk>', views.edit, name='edit'),
    path('edit2/<int:customer_pk>', views.edit2, name='edit2'),
    
    #알림,알림삭제,팀원제의한사람정보
    path('alarm/<int:customer_pk>', views.alarm, name='alarm'),
    path('alarm2/<int:message_pk>', views.alarm2, name='alarm2'),
    path('sender_customer/<int:message_pk>', views.sender_customer, name='sender_customer'),

]
