#!/usr/bin/env python
# * coding: utf-8 *
import json, urllib2
from urllib import urlencode

from datetime import datetime 
from django.core.management import setup_environ

import settings
setup_environ(settings)

from identica.models import Mensaje

#http://diekershoff.homeunix.net/tobias/2011-04-26/using-python-to-update-your-statusnet-account
user = "usuario"
pwd = "XXXXX"
apibase = "https://identi.ca/api"
# connection magic
pwd_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
pwd_mgr.add_password(None, apibase, user, pwd)
handler = urllib2.HTTPBasicAuthHandler(pwd_mgr)
opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)





print("Procesando mensajes pendientes:")
for m in Mensaje.objects.filter(fecha__lte=datetime.now(), enviado=False):
	print "Enviando mensaje: ["+str(m)+"]"
	# now define a message
	msg = "Hi from Python"
	# url encode it nicely and set your own client name – no links in source!
	themsg = urlencode({'status':msg,'source':'mensajero'})
	# and send the notice
	urllib2.urlopen(apibase+'/statuses/update.json?s',themsg)
	m.enviado=True
	m.save()
