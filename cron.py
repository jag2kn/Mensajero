from datetime import datetime 
from django.core.management import setup_environ

import settings
setup_environ(settings)

from identica.models import Mensaje

print("Procesando mensajes pendientes:")
for m in Mensaje.objects.filter(fecha__lte=datetime.now(), enviado=False):
    print "Enviando mensaje: ["+str(m)+"]"
    m.enviado=True
    m.save()
