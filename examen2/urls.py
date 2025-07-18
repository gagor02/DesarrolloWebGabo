from django.urls import path 
from examen2 import views

app_name = 'examen2'

urlpatterns = [
    path('v1/list/tasks/', views.ListTasksAPIView.as_view(), name='list_task_api'),
    path('v1/detail/tasks/<int:pk>/', views.DetailTasksAPIView.as_view(), name='detail_task_api'),
    path('v1/create/tasks/', views.CreateTasksAPIView.as_view(), name='create_task_api'),
    path('v1/update/tasks/<int:pk>/', views.UpdateTasksAPIView.as_view(), name='update_task_api'),
    path('v1/delete/tasks/<int:pk>/', views.DeleteTasksAPIView.as_view(), name='delete_task_api'),

]