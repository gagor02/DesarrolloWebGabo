from django.db import models

# Create your models here.

CHOICES_STATE = (
    ("Sin_Resolver", "SR" ),
    ("Resuelto", "R")
)

class User(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    state = models.CharField(max_length=20, choices=CHOICES_STATE, default="Sin_Resolver")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

    



