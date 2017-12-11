#!/usr/bin/env python
# vi: set foldmethod=indent: set tabstop=2: set shiftwidth=2:
from libs.network.http import http_get
from libs.string.misc import utf8_to_punny
import re
import logging
logger = logging.getLogger (__name__)

IANA_TLDS_WHOIS_LIST_URL = "https://www.iana.org"
RE_EXTRACT_TLD = re.compile ("""^.*<span class="domain tld"><a href="(?P<url>[^"]+)">.(?P<tld>[^<]+)</a>.*$""")
RE_EXTRACT_WHOIS_SERVER = re.compile ("""^.*WHOIS Server:</b>\s(?P<server>.+)$""")
TLDS_LIST_URL = "https://raw.githubusercontent.com/publicsuffix/list/master/public_suffix_list.dat"

def _fetch_from_iana ():
  logger.info ("Début de la récupération des associations TLD / serveur de whois.")
  for l in http_get ("{}/{}".format (IANA_TLDS_WHOIS_LIST_URL, '/domains/root/db')).split ('\n'):
    m = re.match (RE_EXTRACT_TLD, l)
    if m:
      yield (m.group ('tld'), _extract_from_page (m.group ('url')))

def _extract_from_page (page):
  for i in http_get ("{}/{}".format (IANA_TLDS_WHOIS_LIST_URL, page)).split ('\n'):
    n = re.match (RE_EXTRACT_WHOIS_SERVER, i)
    if n:
      return n.group ('server')
    
def fetch_tld_whoisserver_cache ():
  result = {}
  for asso in _fetch_from_iana ():
    if asso[1] not in result:
      result[asso[1]] = []
    logger.info ("{} -> {}".format (*asso))
    result[asso[1]].append (asso[0])
  return result

def fetch_tld_list ():
  result = []
  for l in http_get (TLDS_LIST_URL).split ('\n'):
    l = l.strip ()
    if l and not l.startswith ('//'):
      if l.startswith ('*.'):
        l = l.replace ('*.', '')
      result.append (utf8_to_punny (l))
  return result

