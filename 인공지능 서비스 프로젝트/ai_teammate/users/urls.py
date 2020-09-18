from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signup2/<int:customer_pk>', views.signup2, name='signup2'),
    path('signup3/<int:customer_pk>', views.signup3, name='signup3'),
    path('signup4/<int:customer_pk>', views.signup4, name='signup4'),
    path('signup5/<int:customer_pk>', views.signup5, name='signup5'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('team_no/<int:customer_pk>',views.team_no, name='team_no'),
    path('team_yes/<int:customer_pk>',views.team_yes, name='team_yes'),
    path('study_no/<int:customer_pk>',views.study_no, name='study_no'),
    path('study_yes/<int:customer_pk>',views.study_yes, name='study_yes'),

]