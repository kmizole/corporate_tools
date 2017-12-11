# vi: set foldmethod=indent: set tabstop=2: set shiftwidth=2:
from itertools import product
import logging
from libs.exceptions import WrongDomainException
logger = logging.getLogger (__name__)

_WORDS_SEPARATORS = [ '-', '_' ]


def shuffle_words_from_lists (domain, words_list, combine = False, combine_times = 3):
  possibilities = []
  if combine:
    logger.info ("Activation de la combinaison ({} itérations).".format (combine_times))
    for i in range (0, combine_times):
      possibilities.append ([domain] + words_list)
      possibilities.append (_WORDS_SEPARATORS)
    """Ça, c'est pour enlever le séparateur final."""
    possibilities = possibilities[:-1]
  else:
    logger.info ("Pas de combinaison.")
    possibilities = [
      [ domain ],
      _WORDS_SEPARATORS,
      words_list
    ]
  for temp in product (*possibilities):
    if domain in (temp):
      yield "".join (temp)

def load_domains_from_file (file = None):
  with open (file, 'r') as f:
    for l in f:
      try:
        yield ".".join (extract_domain_tld (l.strip ()))
      except WrongDomainException as e:
        logger.warn (e)

def utf8_to_punny (word):
  return word.encode ('idna').decode ('ascii')
