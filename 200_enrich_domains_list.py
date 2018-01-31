#!/usr/bin/env python3
# vi: set foldmethod=indent: set tabstop=2: set shiftwidth=2:
import argparse
import time
import logging
from libs.string.misc import load_domains_from_file
from libs.network.whois import query
logging.basicConfig (
  format = "[%(asctime)s] - %(levelname)-8s - %(name)-15s - %(message)s",
  level = logging.INFO,
)
logger = logging.getLogger (__name__)

if __name__ == "__main__":
  parser = argparse.ArgumentParser ()
  parser.add_argument ('-i', '--input_file', help = 'Fichier contenant la liste des noms de domaine à requêter.', \
    type = str, required = True)
  parser.add_argument ('-o', '--output_file', help = 'Fichier de rapport.', type = str, default = '/dev/stdout')
  parser.add_argument ('--use-cache', required = False, default = True, \
    help = "Activer ce booléen pour ne pas utiliser le dossier de cache.", \
    action = 'store_false' )
  parser.add_argument ('--cache-file', required = False, default = "cache/tld_whois.py", \
    help = "Fichier de cache.")
  args = parser.parse_args ()

  with open (args.output_file, 'w') as f:
    f.write ("""Domaine;Registrar;Propriétaire;Date Expiration;DNS\n""")
    for domain in load_domains_from_file (args.input_file):
      logger.info ("Traitement du domaine {}".format (domain))
      try:
        d = query (domain, use_cache = args.use_cache, cache_file = args.cache_file)
        line_content = "{};{};{};{};{}\n".format (domain, d['registrar'][0],\
          d['registrant'][0], d['expiration_date'][0], ",".join (d['name_servers']))
        f.write (line_content)
      except (IndexError, TypeError):
        logger.error ("Problème sur la gestion de {}".format (domain))
