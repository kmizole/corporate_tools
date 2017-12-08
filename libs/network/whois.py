#!/usr/bin/env python
# vi: set foldmethod=indent: set tabstop=2: set shiftwidth=2:
import time
import socket
import signal
import logging
from libs.exceptions import TimeoutException, TooManyWhoisRequestsException
from libs.string.tld import get_server_for_tld
from libs.string.misc import extract_domain_tld
from libs.string.whois import parse
logger = logging.getLogger (__name__)

NB_RETRY_ON_EMPTY_RESPONSE = 5
TIME_SLEEP_BEFORE_RETRY = 5

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
      logger.debug ("Réception de {}".format (t))
      response.append(t)
      if t == b'': 
        logger.debug ("On coupe; chaine vide!")
        break

    s.close()
    logger.info ("La requête s'est bien passée.")
  except TimeoutException as e:
    logger.error ("Timeout lors de l'interrogation de {}".format (whois_server))
    return ""
  except Exception as e:
    logger.error ("Problème lors du contact de {}".format (whois_server))
    logger.error (e)
    return ""

  return b''.join(response).decode(errors = 'replace')

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

def query (domain, use_cache = False, cache_file = None):
  whois_server = None
  tld = extract_domain_tld (domain)[1]
  if use_cache:
    """On manipule toujours un itérateur; pour chopper le premier faut utiliser next."""
    whois_server = next (get_server_for_tld (tlds = [ tld ],\
      use_cache = use_cache, cache_file = cache_file))[1]

  raw_data = ""
  for i in range (1, NB_RETRY_ON_EMPTY_RESPONSE):
    raw_data = _do_whois_query (domain, whois_server)
    try:
      return parse (raw_data, tld)
    except TooManyWhoisRequestsException:
      logger.info ("La réponse est vide; on fait une pause et on réessaye.")
      time.sleep (TIME_SLEEP_BEFORE_RETRY * i)
