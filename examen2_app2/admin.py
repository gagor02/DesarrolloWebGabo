from django.contrib import admin

# Register your models here.

from examen2_app2 import models

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellido']

@admin.register(models.Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'state', 'user']