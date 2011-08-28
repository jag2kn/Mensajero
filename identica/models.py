from django.db import models
from django.contrib.auth.models import User
# Define a custom User class to work with django-social-auth

class Mensaje(models.Model):
	mensaje = models.TextField(max_length=140)
	fecha = models.DateTimeField(blank=False, null=False)
	usuario = models.ForeignKey(User)
	enviado = models.BooleanField()
	def __unicode__(self):
		return self.mensaje

