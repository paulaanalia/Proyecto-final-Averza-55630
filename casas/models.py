from django.db import models
from django.contrib.auth.models import User


class Casa(models.Model):
    calle = models.CharField(max_length=50)
    altura = models.IntegerField(null=True)
    piso = models.IntegerField(null=True)
    departamento = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)
    horario = models.TimeField(null=True)
    anfitrion = models.CharField(max_length=50, null=True)
    menu = models.CharField(max_length=100, null=True)

 
    def __str__(self):
        return f'{self.anfitrion}'


class Review(models.Model):
    valoracion = models.PositiveSmallIntegerField()
    comentario = models.CharField(max_length=150)


class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"


   






