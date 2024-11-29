from django.db import models
import os

#python manage.py makemigrations cmd

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nac = models.DateField()
    edad = models.IntegerField(null=True, blank=True)
    lugar = models.CharField(max_length=255, null=True, blank=True)
    foto = models.ImageField(upload_to='clientes_fotos', blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.edad} {self.lugar}"
    
    #Eliminar la foto
    def delete(self, *args, **kwargs):
        if self.foto:
            if os.path.isfile(self.foto.path):
                os.remove(self.foto.path)
            super().delete(*args, **kwargs)