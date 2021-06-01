from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import TaskList, TaskDetail, CreateTask, UpdateTask, DeleteTask, UserLogin, RegisterUser

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterUser.as_view(), name="register"),
    path('', TaskList.as_view(), name='tasklist'),
    #path('task-detail/<int:pk>/', TaskDetail.as_view(), name='taskdetail'),
    path('task-update/<int:pk>/', UpdateTask.as_view(), name='taskupdate'),
    path('task-delete/<int:pk>/', DeleteTask.as_view(), name='taskdelete'),
    path('create/', CreateTask.as_view(), name='taskcreate'),
]