from django.contrib import admin
from django.urls import path
from app.views.user import CreateUser

urlpatterns = [  
    path('user/create/', CreateUser.as_view()),
]
