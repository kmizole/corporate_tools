#!/usr/bin/env python
# vi: set foldmethod=indent: set tabstop=2: set shiftwidth=2:
from libs.network.http import http_get
from libs.string.misc import utf8_to_punny
from libs.exceptions import WrongDomainException
import logging
import json
logger = logging.getLogger (__name__)

def get_server_for_tld (tlds = [ ], use_cache = True, cache_file = 'cache/tld_whois.py'):
  if use_cache == False:
    logger.info ("Récupération des informations sans passer par le fichier de cache.")
    for t in tlds:
      yield (t, _extract_from_page ("/domains/root/db/{}.html".format (utf8_to_punny (t))))
  else:
    try:
      logger.info ("Récupération des informations à partir du fichier de cache {}.".format (cache_file))
      with open (cache_file, 'r') as f:
        temp = json.loads (f.read ())
        for ns in temp:
          for tld in temp[ns]:
            if tld in tlds:
              yield (tld, ns)
    except FileNotFoundError:
      logger.error ("Impossible d'ouvrir le fichier de cache {}; récupération des informations depuis IANA.".format (cache_file))
      for t in tlds:
        yield (t, _extract_from_page ("/domains/root/db/{}.html".format (utf8_to_punny (t))))
    
def _compute_from_iana (element):
  for t in _fetch_from_iana ():
    yield ("{}.{}".format (element, t[0]), t[1])

def compute_all_domains_tld (element, use_cache = True, cache_file = 'cache/tld_whois.py'):
  if use_cache == False:
    logger.info ("Récupération des informations depuis IANA (pas de cache).")
    yield _compute_from_iana (element)
  else:
    try:
      logger.info ("Récupération des informations à partir du fichier de cache {}.".format (cache_file))
      with open (cache_file, 'r') as f:
        temp = json.loads (f.read ())
        for ns in temp:
          for tld in temp[ns]:
            yield ( "{}.{}".format (element, tld), ns )
    except FileNotFoundError:
      logger.error ("Impossible d'ouvrir le fichier de cache {}; récupération des informations depuis IANA.".format (cache_file))
      yield _compute_from_iana (element)

def extract_domain_tld (element):
  temp = element.lower ().split ('.')
  if len (temp) < 2:
    raise WrongDomainException ("{} ne ressemble vraiment pas à un domaine!!!.".format (element))
  return ("".join (temp[:-1]), temp[-1])

def domain_from_element (element):
  try:
    return extract_domain_tld (element)[0]
  except WrongDomainException: 
    return element
