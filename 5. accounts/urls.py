from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.user_profile, name='user-profile'),
    path('<str:username>/follow/', views.follow_user, name='follow-user'),
]
