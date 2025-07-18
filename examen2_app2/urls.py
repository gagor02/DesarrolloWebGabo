from django.urls import path

from examen2_app2 import views

app_name = 'examen2_app2'

urlpatterns = [
    path('list/tasks/', views.TaskList.as_view(), name="list_tasks"),

    # Different lists by attributes
    path('list/tasks/ids', views.TaskListID.as_view(), name="list_tasks_id"), # Lista de todos los pendientes (solo IDs)
    path('list/tasks/ids_titles', views.TaskList.as_view(), name="list_tasks_id_title"), # Lista de todos los pendientes (IDs y Titles)
    path('list/tasks/sr/ids/titles', views.TaskListIDTitleNoCompleted.as_view(), name="list_tasks_sr_id_title"), # Lista de todos los pendientes sin resolver (ID y Title)
    path('list/tasks/r/ids/titles', views.TaskListIDTitleCompleted.as_view(), name="list_tasks_r_id_title"), # Lista de todos los pendientes resueltos (ID y Title)
    path('list/tasks/', views.TaskListIDUserID.as_view(), name="list_tasks_id_userid"), # Lista de todos los pendientes (IDs y userID)
    path('list/tasks/', views.TaskListIDUserIDCompleted.as_view(), name="list_tasks_r_id_userid"), # Lista de todos los pendientes resueltos (ID y userID)
    path('list/tasks/', views.TaskListIDUserIDNoCompleted.as_view(), name="list_tasks_sr_id_userid"), # Lista de todos los pendientes sin resolver (ID y userID)
    

    path('new/tasks/', views.NewTask.as_view(), name="create_tasks"),
    path('detail/tasks/<int:pk>/', views.TaskDetail.as_view(), name="detail_tasks"),
    path('update/tasks/', views.TaskUpdate.as_view(), name="update_tasks"),
    path('delete/tasks/', views.TaskDelete.as_view(), name="delete_tasks"),


    ### User Urls ###
    path('create/user/', views.NewUser.as_view(), name="create_user"),
    path('list/user/', views.UserList.as_view(), name="list_user"),
]