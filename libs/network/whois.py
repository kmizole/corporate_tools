#!/usr/bin/env python
# vi: set foldmethod=indent: set tabstop=2: set shiftwidth=2:
import time
import socket
import signal
import logging
from libs.exceptions import TimeoutException
logger = logging.getLogger (__name__)

"""https://stackoverflow.com/questions/492519/timeout-on-a-function-call"""
def _time_out_handler (signum, frame):
  raise TimeoutException ("Timeout!")

signal.signal (signal.SIGALRM, _time_out_handler)

def _do_whois_query (domain, whois_server = None):
  if not whois_server:
    logger.debug ("Serveur de whois non fourni, supposition en cours.")
    whois_server = '{}.whois-servers.net'.format (domain.split ('.')[-1])

  logger.info ("Utilisation du serveur {} pour whois sur domaine {}.".format (whois_server, domain))
  response = []

  signal.alarm (10)
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(((whois_server, 43)))
    s.send(("%s\r\n" % domain).encode())
    while 1:
      t = s.recv(4096)
      response.append(t)
      if t == b'': break

    s.close()
  except TimeoutException as e:
    logger.error ("Timeout lors de l'interrogation de {}".format (whois_server))
    return ""
  except Exception as e:
    logger.error ("Problème lors du contact de {}".format (whois_server))
    logger.error (e)
    return ""

  return b''.join(response).decode()

def estimate_domain_is_registered (domain, whois_server = None):
  for l in _do_whois_query (domain = domain, whois_server = whois_server).lower ().split ('\n'):
    if 'nserver' in l:
      logger.info ("On considère que le domaine {} est réservé car présence d'un enregistrement contenant nserver.".format (domain))
      return True
    if 'name' in l and 'server' in l:
      logger.info ("On considère que le domaine {} est réservé car présence d'un enregistrement contenant name & server.".format (domain))
      return True
  logger.info ("Je pense que le domaine {} n'est pas réservé.".format (domain))
  return False

