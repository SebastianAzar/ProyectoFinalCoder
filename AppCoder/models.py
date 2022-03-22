from django.db import models

# Create your models here.

class Categoria(models.Model):

    categoria=models.CharField(max_length=40)
    piloto=models.CharField(max_length=40)
    año=models.IntegerField(max_length=4)

class Auto(models.Model):

    marca = models.CharField(max_length=40)
    chasis = models.CharField(max_length=40)
    tipo = models.CharField(max_length=4)
    motor = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.marca}, {self.chasis}, {self.tipo}, {self.motor}'

class Equipo(models.Model):

    nombre=models.CharField(max_length=40)
    direccion=models.CharField(max_length=40)
    año_inicio=models.IntegerField(max_length=4)


