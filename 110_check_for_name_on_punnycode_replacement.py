#!/usr/bin/env python
# vi: set foldmethod=indent: set tabstop=2: set shiftwidth=2:
import argparse
import sys
import logging
logging.basicConfig (
  format = "[%(asctime)s] - %(levelname)-8s - %(name)-15s - %(message)s",
  level = logging.INFO,
)

from libs.exceptions import ParameterException
from libs.string.punny import derivate_domains
from libs.string.misc import extract_domain_tld
from libs.string.tld import get_server_for_tld
from libs.network.nslookup import lookup
from libs.network.whois import estimate_domain_is_registered

SEP_LINE = """+-{:-<25}-+-{:->40}-+-{:->25}-+-{:->8}-+-{:->15}-+\n""".format ("", "", "", "", "")
HEADERS = [ 'Domaine', 'Encodage PunnyCode', 'Encodage UTF-8', 'Réservé?' , '@IPv4?' ]

logger = logging.getLogger (__name__)

def run (**kwargs):
  for i in [ 'domain', 'adapter', 'use_cache', 'cache_file' ]:
    if i not in kwargs:
      raise Exception ("La fonction n'est pas appellée correctement.")
  try:
    (domain, tld) = extract_domain_tld (kwargs['domain'])
    """ Petite astuce, on est sur un itérateur; on en veut le premier."""
    whois_server = next (get_server_for_tld (tlds = [ tld ], use_cache = kwargs['use_cache'], cache_file = kwargs['cache_file']))[1]
    for punny_domain in derivate_domains (domain):
      punny = "{}.{}".format (punny_domain[1], tld)
      punny_reserved = "Non"
      if estimate_domain_is_registered (punny, whois_server = whois_server):
        punny_reserved = "Oui"

      punny_ip = lookup (punny, kwargs['adapter'])
      if not punny_ip:
        punny_ip = 'N/A'

      utf8 = "{}.{}".format (punny_domain[0], tld)
      yield [ kwargs['domain'], punny, utf8, punny_reserved, punny_ip ]
  except ParameterException as e:
    logger.critical (e)

if __name__ == "__main__":

  parser = argparse.ArgumentParser(description='Génération de tout plein de noms de domaines potentiels pour surveiller le phishing.')
  parser.add_argument('-d', '--domain', type = str, required = True, \
    help = 'Adresse du domaine à surveiller (Option duplicable 1 fois par domaine).',\
    dest = 'domain', action = 'append')
  parser.add_argument('-a', '--adapter', type = str, required = False, \
    help = 'Adapteur à utiliser pour réaliser la résolution DNS.', default = 'dns', \
    dest = 'adapter')
  parser.add_argument ('-o', '--output', type = argparse.FileType ('w'), \
    default = sys.stdout, help = "Emplacement du rapport.", dest = 'output' )
  parser.add_argument ('--use-cache', required = False, default = True, \
    help = "Activer ce booléen pour ne pas utiliser le dossier de cache.", \
    action = 'store_false' )
  parser.add_argument ('--cache-file', required = False, default = "cache/tld_whois.py", \
    help = "Fichier de cache.")
  args = parser.parse_args ()

  args.output.write (SEP_LINE)
  args.output.write ("""| {:<25} | {:>40} | {:>25} | {:>8} | {:>15} |\n""".format (*HEADERS))
  args.output.write (SEP_LINE)

  try:
    for current_domain in args.domain:
      for l in run (domain = current_domain, adapter = args.adapter, \
        use_cache = args.use_cache, cache_file = args.cache_file):
        args.output.write ("""| {:<25} | {:>40} | {:>25} | {:>8} | {:>15} |\n""".format (*l))
      args.output.write (SEP_LINE)
  except Exception as e:
    logger.critical ("Erreur catastrophique : {}".format (e))
