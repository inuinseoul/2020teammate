from django.urls import path
from . import views


app_name = "newsletter"
urlpatterns = [
    path('',views.news_select,name='select'),
    path("art", views.news_art_list, name="art"),
    path("economy", views.news_economy_list, name="economy"),
    path("social", views.news_social_list, name="social"),
    path("health", views.news_health_list, name="health"),
    path("tech", views.news_tech_list, name="tech"),
    path("all", views.news_all_list, name="all"),
]