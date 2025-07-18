from django import forms 

from examen2_app2 import models

class NewTaskForm(forms.ModelForm):
    class Meta:
        model = models.Tasks
        fields = ['title', 'description', 'state', 'user']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'type':'text', 'class':'form-control', 'rows': 3, 'placeholder': 'Write a description for the task'}),
            'state': forms.Select(attrs={'type':'select', 'class': 'form-control'}),
            'user': forms.Select(attrs={'type':'select','class': 'form-control'}),
        }

class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model =models.Tasks
        fields = ['title', 'description', 'state', 'user']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'type':'text', 'class':'form-control', 'rows': 3, 'placeholder': 'Write a description for the task'}),
            'state': forms.Select(attrs={'type':'select', 'class': 'form-control'}),
            'user': forms.Select(attrs={'type':'select','class': 'form-control'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['nombre', 'apellido']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
        }