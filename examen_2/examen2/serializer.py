from rest_framework import serializers
from examen2_app2.models import Tasks

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'title', 'description', 'state', 'user']

class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = "__all__"

class NewTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = "__all__"

class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'title', 'description', 'state', 'user']




