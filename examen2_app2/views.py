from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.

from examen2_app2 import models
from examen2_app2 import forms

### CRUD Tareas pros ###

# Create

class NewTask(generic.CreateView):
    template_name = 'examen2_app2/create_task.html'
    model = models.Tasks
    form_class = forms.NewTaskForm
    success_url = reverse_lazy('examen2_app2:task_list')

# Read

## List
class TaskList(generic.View):
    template_name = 'examen2_app2/task_list.html'
    context = {}

    def get(self, request):
        self.context = {
            "tasks": models.Tasks.objects.all()
        }
        return render(request, self.template_name, self.context)

# List by ID

class TaskListID(generic.View):
    template_name = 'examen2_app2/task_list_ids.html'
    context = {}

    def get(self, request):
        self.context = {
            "tasks": models.Tasks.objects.all()
        }
        return render(request, self.template_name, self.context)
    
# List by ID and Title

class TaskListIDTitle(generic.View):
    template_name = 'examen2_app2/task_list_idstitles.html'
    context = {}

    def get(self, request):
        self.context = {
            "tasks": models.Tasks.objects.all()
        }
        return render(request, self.template_name, self.context)
    
# List by ID and Title no completed

class TaskListIDTitleNoCompleted(generic.View):
    template_name = 'examen2_app2/nocompleted_task_list_idstitles.html'
    context = {}

    def get(self, request):
        self.context = {
            "tasks": models.Tasks.objects.filter(state='SR')
        }
        return render(request, self.template_name, self.context)
    
# List by ID and Title completed

class TaskListIDTitleCompleted(generic.View):
    template_name = 'examen2_app2/completed_task_list_idstitles.html'
    context = {}

    def get(self, request):
        self.context = {
            "tasks": models.Tasks.objects.filter(state='R')
        }
        return render(request, self.template_name, self.context)
    

# List by ID and UserID

class TaskListIDUserID(generic.View):
    template_name = 'examen2_app2/task_list_ids_userids.html'
    context = {}

    def get(self, request):
        self.context = {
            "tasks": models.Tasks.objects.all()
        }
        return render(request, self.template_name, self.context)
    

# List by ID and UserID completed

class TaskListIDUserIDCompleted(generic.View):
    template_name = 'examen2_app2/completed_task_list_ids_userids.html'
    context = {}

    def get(self, request):
        self.context = {
            "tasks": models.Tasks.objects.filter(state='R')
        }
        return render(request, self.template_name, self.context)
    
# List by ID and UserID no completed

class TaskListIDUserIDNoCompleted(generic.View):
    template_name = 'examen2_app2/nocompleted_task_list_ids_userids.html'
    context = {}

    def get(self, request):
        self.context = {
            "tasks": models.Tasks.objects.filter(state='SR')
        }
        return render(request, self.template_name, self.context)
    

    
## Details
class TaskDetail(generic.View):
    template_name = "examen2_app2/task_detail.html"
    context = {}

    def get(self, request, pk):
        self.context = {
            "tasks": models.Tasks.objects.get(pk=pk)
        }
        return render(request, self.template_name, self.context)
    
#Update 

class TaskUpdate(generic.UpdateView):
    template_name = 'examen2_app2/update_task.html'
    model = models.Tasks
    forms_class = forms.TaskUpdateForm
    success_url = reverse_lazy('examen2_app2:task_list')

# Delete

class TaskDelete(generic.DeleteView):
    template_name = 'examen2_app2/delete_task.html'
    model = models.Tasks
    success_url = reverse_lazy('examen2_app2:task_list')


### CR Usuarios Pros ###

# Create 

class NewUser(generic.CreateView):
    template_name = 'examen2_app2/create_user.html'
    model = models.User
    form_class = forms.UserForm
    success_url = reverse_lazy('examen2_app2:list_user')

# Read

class UserList(generic.ListView):
    template_name = 'examen2_app2/user_list.html'
    context = {}

    def get(self, request):
        self.context = {
            "users": models.User.objects.all()
        }
        return render(request, self.template_name, self.context)
    

    



    


