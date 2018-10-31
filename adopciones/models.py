from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Perfiles(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    web = models.URLField(blank=True)

    def __str__(self): 
        return self.usuario.username

@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Perfiles.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.perfiles.save()

class Mascotas(models.Model):
    nombre = models.CharField(max_length=200)
    raza = models.CharField(max_length=200)
    estado = models.CharField(max_length=200, blank=True)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='rescatados', verbose_name='Imágen')


class Registrado(models.Model):
    email = models.EmailField()
    rut = models.CharField(max_length=13, blank=False, null=True)
    telefono = models.IntegerField(null=True)
    nombres = models.CharField(max_length=23, blank=False, null=True)
    apellidos = models.CharField(max_length=23, blank=False, null=True)
    def __unicode__(self):
        return self.email

    def __str__(self):
        return self.email
