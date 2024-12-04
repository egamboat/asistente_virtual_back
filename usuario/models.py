from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator


class SolicitudAyuda(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="solicitudes")
    correo = models.EmailField()
    texto = models.TextField(validators=[MaxLengthValidator(200)])
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solicitud de {self.usuario.username} - {self.correo}"
