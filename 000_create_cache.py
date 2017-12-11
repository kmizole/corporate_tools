#!/usr/bin/env python
# vi: set foldmethod=indent: set tabstop=2: set shiftwidth=2:
import argparse
import sys
import logging
import json
logging.basicConfig (
  format = "[%(asctime)s] - %(levelname)-8s - %(name)-15s - %(message)s",
  level = logging.INFO,
)
from libs.network.caches import fetch_tld_whoisserver_cache, fetch_tld_list
logger = logging.getLogger (__name__)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Génération des différents fichiers de cache utilisés par les scripts.')
  parser.add_argument('--cache-tld-list', type = argparse.FileType ('w'), \
    help = 'Emplacement du fichier contenant la liste des TLDs.',\
    dest = 'cache_tld_list', required = False, default = None)
  parser.add_argument('--cache-tld-whois', type = argparse.FileType ('w'), \
    help = 'Emplacement du fichier contenant l\'association entre TLD & serveur de whois.',\
    dest = 'cache_tld_whois', required = False, default = None)
  args = parser.parse_args ()
  logger.debug ("Arguments utilisés par le script : {}.".format (args))

  logger.info ("Début de la génération des caches.")
  if args.cache_tld_whois:
    logger.info ("Rafraîchissement du cache pour les associations tld <=> serveur de whois.")
    result = fetch_tld_whoisserver_cache ()
    args.cache_tld_whois.write (json.dumps (result, sort_keys = True, indent = 2))

  if args.cache_tld_list:
    logger.info ("Rafraîchissement du cache pour les TLDs reconnus.")
    result = fetch_tld_list ()
    args.cache_tld_list.write (json.dumps (result, sort_keys = True, indent = 2))
  logger.info ("Fin de la génération des caches.")
