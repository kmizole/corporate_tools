#!/usr/bin/env python
# vi: set foldmethod=indent: set tabstop=2: set shiftwidth=2:
import argparse
import logging
import json
from libs.network.whois import _do_whois_query
from libs.string.whois import parse
from libs.string.misc import extract_domain_tld
logging.basicConfig (
  format = "[%(asctime)s] - %(levelname)-8s - %(name)-15s - %(message)s",
  level = logging.DEBUG,
)
logger = logging.getLogger (__name__)

if __name__ == "__main__":
  parser = argparse.ArgumentParser ()
  parser.add_argument ('-d', '--domain', help = 'Domaine pour lequel on veut récupérer les informations de whois.', \
    type = str, required = True)
  args = parser.parse_args ()

  whois_data = _do_whois_query (args.domain)
  tld = extract_domain_tld (args.domain)[1]
  data = parse (whois_data, tld)
  for k in [ 'creation_date', 'expiration_date', 'updated_date' ]:
    data[k] = str (data[k][0])
  print (whois_data)
  print ("----------------------------------------------")
  print (json.dumps (data, sort_keys = True, indent = 4))
