from django.urls import path
from rest_framework import routers


from auth_ import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('user/', views.MainUserAPIView.as_view()),
]
