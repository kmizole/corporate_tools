#!/usr/bin/env python
# vi: set foldmethod=indent: set tabstop=2: set shiftwidth=2:
import logging
import datetime
from importlib import import_module
import re
from libs.exceptions import TooManyWhoisRequestsException
logger = logging.getLogger (__name__)

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
  -> Sinon, faut charger la liste des expressions régulières présentes dans le dossier libs/strings/whois/tld.py
  -> Ensuite, la fonction _adjust fait l'ajustement des différents formats.
  """
  if _is_to_many_requests (raw_data):
    raise TooManyWhoisRequestsException ("Trop de requêtes trop rapprochées.")
  raw_data=raw_data.replace('\r','')
  logger.debug ("Raw Data reformat : {}".format (raw_data))
  
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
  
  logger.debug ("Chargement du parser pour le tld {}".format (tld))
  try :
    module = import_module ('libs.string.whois_parsers.{}'.format (tld))
    cur_parser = "{}.py".format (tld)
  except ImportError :
    module = import_module ('libs.string.whois_parsers.default')
    cur_parser = "default.py"
  
  logger.info ("Parser utilisé : {}".format (cur_parser)) 
  parser = getattr (module, 'parser')
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
      logger.debug ("avant : {}".format (values))
      """
      Ici on traite les retours à la con en full text (genre du whois uk) avec des \n
      et qui se retrouve en forme de tableau bizarre grace au regex de type ((kldlgj)+)
      => 2 groupes au lieu d'un et donc ça se comporte mal. On remet ça dans la forme standard
      """
      if isinstance (values[0], tuple):
        values = [v for v in values[0][0].split('\n')[:-1]]
        logger.debug ("Values (is instance) : {}".format (values))
      logger.debug ("Values : {}".format (values))
      for m in values:
        logger.debug ("Ajout de {}".format (m))
        r[k].append (m)
  return _adjust (r)
    
