#!/usr/bin/env python
# vi: set foldmethod=indent: set tabstop=2: set shiftwidth=2:
from importlib import import_module
import datetime
import logging
import re
import signal
import socket
import time
from libs.exceptions import TimeoutException, TooManyWhoisRequestsException
from libs.string.tld import get_server_for_tld
from libs.string.misc import extract_domain_tld
logger = logging.getLogger (__name__)

NB_RETRY_ON_EMPTY_RESPONSE = 5
TIME_SLEEP_BEFORE_RETRY = 5
DATE_FORMATS = [
  '%d-%b-%Y',            # 02-jan-2000
  '%d.%m.%Y',            # 02.02.2000
  '%d/%m/%Y',            # 01/06/2011
  '%d-%m-%Y',            # 01/06/2011
  '%Y-%m-%d',            # 2000-01-02
  '%Y.%m.%d',            # 2000.01.02
  '%Y/%m/%d',            # 2005/05/30

  '%Y.%m.%d %H:%M:%S',      # 2002.09.19 13:00:00
  '%Y%m%d %H:%M:%S',          # 20110908 14:44:51
  '%Y-%m-%d %H:%M:%S',        # 2011-09-08 14:44:51
  '%d.%m.%Y  %H:%M:%S',      # 19.09.2002 13:00:00
  '%d-%b-%Y %H:%M:%S %Z',      # 24-Jul-2009 13:20:03 UTC
  '%Y/%m/%d %H:%M:%S (%z)',    # 2011/06/01 01:05:01 (+0900)
  '%Y/%m/%d %H:%M:%S',      # 2011/06/01 01:05:01
  '%a %b %d %H:%M:%S %Z %Y',    # Tue Jun 21 23:59:59 GMT 2011
  '%a %b %d %Y',          # Tue Dec 12 2000
  '%d-%B-%Y',          # 08-june-2004
  '%d-%b-%Y %H:%M:%S',          # 08-jun-2004 12:13:14
  '%Y-%m-%dT%H:%M:%S',      # 2007-01-26T19:10:31
  '%Y-%m-%dT%H:%M:%SZ',      # 2007-01-26T19:10:31Z
  '%Y-%m-%dT%H:%M:%S%z',      # 2011-03-30T19:36:27+0200
  '%Y-%m-%dT%H:%M:%S.%f%z',    # 2011-09-08T14:44:51.622265+03:00
  '%Y-%m-%dt%H:%M:%S.%f',      # 2011-09-08t14:44:51.622265
  '%Y-%m-%dt%H:%M:%S.0z',      # 2011-09-08t14:44:51.0z
  '%Y-%m-%dt%H:%M:%S.000z',         # 2011-09-08t14:44:51.000z
  '%Y%m%d',                 # 20171129
]
NO_CONVERT_CONSTANTS = [ 'CHAMP_ABSENT_DU_RÉFÉRENTIEL' ]

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

  signal.alarm ( NB_RETRY_ON_EMPTY_RESPONSE * TIME_SLEEP_BEFORE_RETRY + 1 )
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
    except TimeoutException as e:
      logger.error ("Timeout lors de l'interrogation pour {}".format (domain))
      return parse ("", tld)

def _is_to_many_requests (raw_data):
  if 'too many requests' in raw_data.lower ():
    return True
  return False

def _string_to_date (string):
  if string in NO_CONVERT_CONSTANTS:
    return string
  elif not string:
    return ''
  string = string.strip().lower()

  for format in DATE_FORMATS:
    try: 
      return datetime.datetime.strptime(string, format)
    except ValueError as e: 
      pass

  logger.error ("Format de date inconnu : {}".format (string))
  return ""

def _adjust (parsed_data):
  result = {}
  for k in parsed_data:
    result[k] = []
    for v in parsed_data[k]:
      v = v.strip ()
      if k in [ 'creation_date', 'expiration_date', 'updated_date' ]:
        v = _string_to_date (v)
      elif k in [ 'name_servers' ]:
        v = v.lower ()

      if v not in result[k]:
        result[k].append (v)
  return result

def parse (raw_data, tld):
  """
Algorithme : 
  -> Si ça contient 'too many requests', on est en train de pêter un droit d'accès. J'exceptionne.
  -> Sinon, faut charger la liste des expressions régulières présentes dans le dossier libs/network/whois_parser/<TLD>.py
  -> Ensuite, la fonction _adjust fait l'ajustement des différents formats.
  """
  if _is_to_many_requests (raw_data):
    raise TooManyWhoisRequestsException ("Trop de requêtes trop rapprochées.")
  
  r = {
    'domain_name': [],
    'registrar': [],
    'registrant': [],
    'creation_date': [],
    'expiration_date': [],
    'updated_date': [],
    'name_servers': [],
    'status': [],
  }
  tld = tld.lower ()
  try:
    logger.debug ("Chargement du parser pour le tld {}".format (tld))
    parser = getattr (import_module ('libs.network.whois_parsers.{}'.format (tld)), 'parser')
    for k, v in parser.items ():
      logger.debug ("Traitement de la clef {}".format (k))
      if v[0] is None:
        logger.debug ("Expression rationnelle None => ajout de {}".format (v[1]))
        r[k].append ( v[1] )
      else:
        logger.debug ("Expression rationnelle définie à compiler.")
        matches = re.compile (v[0]).findall (raw_data)
        logger.debug ("Matches : {}".format (matches))
        values = matches or [ v[1] ]
        logger.debug ("Values : {}".format (values))
        for m in values:
          logger.debug ("Ajout de {}".format (m))
          r[k].append (m)
    return _adjust (r)
  except ModuleNotFoundError:
    logger.error ("Impossible de charger le parser pour le domaine {}".format (tld))
    return None

