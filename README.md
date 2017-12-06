Plusieurs outils & bibliothèques utilisés dans le service pour faire des choses.

# Installation
```
python -m venv <NOM_ENVIRONNEMENT_VIRTUEL>
source <NOM_ENVIRONNEMENT_VIRTUEL>/bin/activate
git clone https://github.com/yapoc/corporate_tools.git
cd corporate_tools
pip install -r requirements
```

# Utilisation
```
source <NOM_ENVIRONNEMENT_VIRTUEL>/bin/activate
cd corporate_toools
./BATCH.py
```

# Description des batchs
Tous les batchs disposent de l'option `-h` (ou `--help`) qui permet de connaitre les options utilisées par le traitement.

## `000_create_cache.py`
  * Va parcourir le site `https://www.iana.org` pour identifier chaque TLD référencé. 
  * Récupère le serveur de `whois` correspondant à  chaque TLD.
  * Enregistre l'association dans un tableau json tel que : 

```
{ 
  "serveur_whois1" : [ "tld1_1", "tld1_2" ],
  "serveur_whois2" : [ "tld2_1" ],
}
```
  * Il est important que le dossier de cache soit présent sur le système de fichiers. Par défaut, c'est le dossier `cache`.

## Script `100_check_for_name_on_each_tld.py`
  * À partir du mot indiqué via l'option `-n`, le script va vérifier que le domaine existe sur l'ensemble des TLDs connus.
  * Si on utilise le cache, il ne requête pas trop l'IANA comme un bourrin.
  * Si on utilise pas le cache, il "reconstruit" le cache à chaque opération pour connaitre le serveur de WHOIS affecté à chaque TLD.
  * Un exemple de résultat : 

```
(VirtualEnv) [user@host corporate_tools]$ ./100_check_for_name_on_each_tld.py -n sample
+-----------------------------------------------+----------+-----------------+
| Domaine                                       | Réservé? |          @IPv4? |
+-----------------------------------------------+----------+-----------------+
| sample.africa                                 |      Non |             N/A |
| sample.capetown                               |      Non |             N/A |
| sample.cc                                     |      Oui |   43.242.35.123 |
|                                     8<...>8                                |
+-----------------------------------------------+----------+-----------------+
```
