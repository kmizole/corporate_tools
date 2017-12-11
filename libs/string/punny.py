# vi: set foldmethod=indent: set tabstop=2: set shiftwidth=2:
from itertools import product
from libs.string.tld import domain_from_element
from libs.string.misc import utf8_to_punny
import logging
logger = logging.getLogger (__name__)

_REPLACEMENTS = {
  'a': ['ä', 'à', 'á'],
  'e': ['ë', 'è', 'é'],
  'i': ['ï', 'ì', 'í'],
  'o': ['ö', 'ò', 'ó', '0'],
  'u': ['ü', 'ù', 'ú'],
  'm': ['rn'],
  's': ['5'],
  'b': ['6'],
  'g': ['q', '9'],
  'd': ['cl'],
  'w': ['vv'],
}

def _build_letters_tree (word):
  result = []
  for letter in word:
    temp = [ letter ]
    if letter in _REPLACEMENTS:
      temp += _REPLACEMENTS [letter]
    result.append (temp)
  return result

def derivate_domains (domain):
  domain = domain_from_element (domain)
  logger.info ("Tentative d'identification des domaines dérivés de {}".format (domain))
  possibilities = _build_letters_tree (domain)
  logger.debug ("Produits cartésiens qu'il va falloir se fader.".format (possibilities))
  for temp in product (*possibilities):
    current = "".join (temp)
    yield ("{}".format (current), "{}".format (utf8_to_punny (current)))
