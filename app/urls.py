from django.contrib import admin
from django.urls import path
from app.views.user import CreateUser, LoginView, RetrieveUser, UpdateUser, DeleteUser

urlpatterns = [  
    path('user/create/', CreateUser.as_view()),
    path('user/login/', LoginView.as_view()),
    path('user/<int:pk>/', RetrieveUser.as_view()),
    path('user/update/', UpdateUser.as_view()),
    path('user/delete/<int:pk>/', DeleteUser.as_view()),
]
