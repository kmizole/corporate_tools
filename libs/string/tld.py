#!/usr/bin/env python
# vi: set foldmethod=indent: set tabstop=2: set shiftwidth=2:
from libs.network.http import http_get
from libs.string.punny import utf8_to_punny
import re
import logging
import json
logger = logging.getLogger (__name__)

TLDS_LIST_URL = "https://www.iana.org"
RE_EXTRACT_TLD = re.compile ("""^.*<span class="domain tld"><a href="(?P<url>[^"]+)">.(?P<tld>[^<]+)</a>.*$""")
RE_EXTRACT_WHOIS_SERVER = re.compile ("""^.*WHOIS Server:</b>\s(?P<server>.+)$""")

def _fetch_from_iana ():
  logger.info ("Début de la récupération des associations TLD / serveur de whois.")
  for l in http_get ("{}/{}".format (TLDS_LIST_URL, '/domains/root/db')).split ('\n'):
    m = re.match (RE_EXTRACT_TLD, l)
    if m:
      yield (m.group ('tld'), _extract_from_page (m.group ('url')))

def _extract_from_page (page):
  for i in http_get ("{}/{}".format (TLDS_LIST_URL, page)).split ('\n'):
    n = re.match (RE_EXTRACT_WHOIS_SERVER, i)
    if n:
      return n.group ('server')
    
def _get_ns_tlds_mapping_from_iana ():
  result = {}
  for asso in _fetch_from_iana ():
    if asso[1] not in result:
      result[asso[1]] = []
    logger.info ("{} -> {}".format (*asso))
    result[asso[1]].append (asso[0])
  return result

def get_server_for_tld (tlds = [ ]):
  for t in tlds:
    yield (t, _extract_from_page ("/domains/root/db/{}.html".format (utf8_to_punny (t))))


def create_cache_data ():
  return _get_ns_tlds_mapping_from_iana ()

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
