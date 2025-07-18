from django.urls import path

from examen2_app2 import views

app_name = 'examen2_app2'

urlpatterns = [
    path('list/tasks/', views.TaskList.as_view(), name="list_tasks"),
    path('new/tasks/', views.NewTask.as_view(), name="create_tasks"),
    path('detail/tasks/<int:pk>/', views.TaskDetail.as_view(), name="detail_tasks"),
    path('update/tasks/', views.TaskUpdate.as_view(), name="update_tasks"),
    path('delete/tasks/', views.TaskDelete.as_view(), name="delete_tasks"),

    ### User Urls ###
    path('create/user/', views.NewUser.as_view(), name="create_user"),
    path('list/user/', views.UserList.as_view(), name="list_user"),
]