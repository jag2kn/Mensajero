from django.db import models
from django.contrib.auth.models import User
# Define a custom User class to work with django-social-auth

class Mensaje(models.Model):
	mensaje = models.CharField(max_length=140)
	fecha = models.DateField()
	usuario = models.ForeignKey(User)
	def __unicode__(self):
		return self.mensaje

