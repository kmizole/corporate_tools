#!/usr/bin/env python3
# vi: set foldmethod=indent: set tabstop=2: set shiftwidth=2:
import argparse
import logging
import json
import sys
from libs.network.whois import _do_whois_query
from libs.string.misc import extract_domain_tld
from libs.string.tld import get_server_for_tld
from libs.string.whois import parse
logging.basicConfig (
  format = "[%(asctime)s] - %(levelname)-8s - %(name)-15s - %(message)s",
  level = logging.DEBUG,
)
logger = logging.getLogger (__name__)

if __name__ == "__main__":
  parser = argparse.ArgumentParser ()
  parser.add_argument ('-d', '--domain', help = 'Domaine pour lequel on veut récupérer les informations de whois.', \
    type = str, required = True)
  parser.add_argument ('-c', '--cache-file', help = 'Emplacement du fichier de cache.', \
    type = str, required = False)
  args = parser.parse_args ()

  whois_server = None
  tld = extract_domain_tld (args.domain)[1]
  if args.cache_file:
    """Plaisir de bourgeois, le cas est traité dans la lib & elle va se connecter à l'IANA pour récupérer le serveur. Mais c'est vendredi, j'ai envie."""
    try:
      f = open (args.cache_file, 'r')
      f.close ()
    except FileNotFoundError as e:
      logger.error ("Le fichier de cache n'est pas accessible en lecture.")
      sys.exit ('')
      
    whois_server = next (get_server_for_tld (tlds = [ tld ],\
      use_cache = True, cache_file = args.cache_file))[1]
  else:
    """Extract whois server a la volee"""
    whois_server = next (get_server_for_tld (tlds = [ tld ], use_cache = False))[1]
  
  whois_data = _do_whois_query (args.domain, whois_server = whois_server)
  data = parse (whois_data, tld)
  for k in [ 'creation_date', 'expiration_date', 'updated_date' ]:
    try:
      data[k] = str (data[k][0])
    except (IndexError, TypeError):
      continue
  print (whois_data)
  print ("----------------------------------------------")
  print (json.dumps (data, sort_keys = True, indent = 4))
