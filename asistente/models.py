# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Agenda(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="agenda")

    def __str__(self):
        return f"Agenda de {self.usuario.username}"


class TipoEvento(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

class Modalidad(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Modalidades"

class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE, related_name="eventos")
    titulo = models.CharField(max_length=150, default='Sin título')
    tipo_evento = models.ForeignKey(TipoEvento, on_delete=models.CASCADE, related_name="eventos")
    modalidad = models.ForeignKey(Modalidad, on_delete=models.CASCADE, related_name="eventos")
    descripcion = models.CharField(max_length=200)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField(null=True, blank=True)
    google_event_id = models.CharField(max_length=100, null=True, blank=True, unique=True)  # Id de eventos de Google

    def __str__(self):
        return self.descripcion
