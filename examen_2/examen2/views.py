from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from examen2_app2.models import Tasks
from .serializer import TaskListSerializer, TaskUpdateSerializer, NewTaskSerializer, TaskDetailSerializer

# Create your views here.

### API ###

# Create
class CreateTasksAPIView(generics.CreateAPIView):
    serializer_class = NewTaskSerializer

## List

class ListTasksAPIView(APIView):
    def get(self, request):
        queryset = Tasks.objects.all()
        data = TaskListSerializer(queryset, many=True).data
        return Response(data)
    
## Detail

class DetailTasksAPIView(APIView):
    def get(self, request, pk):
        queryset = Tasks.objects.get(pk=pk)
        data = TaskDetailSerializer(queryset, many=False).data
        return Response(data)
    
# Update

class UpdateTasksAPIView(generics.UpdateAPIView):
    serializer_class = TaskUpdateSerializer
    queryset = Tasks.objects.all()

# Delete

class DeleteTasksAPIView(generics.DestroyAPIView):
    serializer_class = TaskDetailSerializer
    queryset = Tasks.objects.all()

