import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

# Create your models here.

class Tusuarios(AbstractUser):
    biografia = models.TextField()
    ROLES = [
        ('organizador','Organizador'),
        ('participante', 'Participante'),
    ]

    rol = models.CharField(max_length=20, choices=ROLES, default='participante')

    def __str__(self):
        return self.first_name

class Teventos(models.Model):
    organizador = models.ForeignKey('Tusuarios', models.DO_NOTHING)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_hora = models.DateTimeField(default=datetime.now())
    capacidad_maxima = models.CharField(max_length=200)
    imagen_url = models.CharField(max_length=200)

    def __str__(self):
        return "[" +self.organizador.first_name + "]" +self.titulo

class Tcomentarios(models.Model):
    usuario = models.ForeignKey('Tusuarios', models.DO_NOTHING)
    evento = models.ForeignKey('Teventos', models.DO_NOTHING)
    comentario = models.TextField(max_length=2000)
    fecha_publicacion = models.DateTimeField(db_column='fecha_comentario')

    def __str__(self):
        return "[" + self.usuario.first_name + "] [" + self.evento.titulo + "]" +self.comentario

class Treservas(models.Model):
    evento = models.ForeignKey('Teventos', models.DO_NOTHING)
    usuario = models.ForeignKey('Tusuarios', models.DO_NOTHING, )
    entradas = models.IntegerField()
    TIPO_RESERVA = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada')
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_RESERVA, default='pendiente')

    def __str__(self):
        return self.evento.titulo