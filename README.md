Plusieurs outils & bibliothèques utilisés dans le service pour faire des choses.

# Installation
```
python3 -m venv <NOM_ENVIRONNEMENT_VIRTUEL>
source <NOM_ENVIRONNEMENT_VIRTUEL>/bin/activate
git clone https://github.com/kmizole/corporate_tools.git
cd corporate_tools
pip install -r requirements
```

# Utilisation
```
source <NOM_ENVIRONNEMENT_VIRTUEL>/bin/activate
cd corporate_toools
./BATCH.py
```

# Description des traitements
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

## `100_check_for_name_on_each_tld.py`
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

## `005_test_whois_parser.py`
  * À partir du domaine indiqué via l'option `-d`.
  * Fait la requête whois.
  * Tente de la parser.
  * Je m'en sers surtout pour afficher les messages de `debug` & tester unitairement les parsers.
  * Un exemple de résultat : 

```
(VirtualEnv) [user@host corporate_tools]$ ./005_test_whois_parser.py -d example.org
[2017-12-08 10:49:10,854] - DEBUG    - libs.network.whois - Serveur de whois non fourni, supposition en cours.
[2017-12-08 10:49:10,855] - INFO     - libs.network.whois - Utilisation du serveur org.whois-servers.net pour whois sur domaine example.org.
        8<...>8
[2017-12-08 10:49:11,119] - DEBUG    - libs.network.whois - Réception de b'Domain [2017-12-08 10:49:11,137] - DEBUG    - libs.string.whois - Traitement de la clef updated_date
[2017-12-08 10:49:11,137] - DEBUG    - libs.string.whois - Expression rationnelle définie à compiler.
[2017-12-08 10:49:11,138] - DEBUG    - libs.string.whois - Matches : []
[2017-12-08 10:49:11,138] - DEBUG    - libs.string.whois - Values : ['']
[2017-12-08 10:49:11,139] - DEBUG    - libs.string.whois - Ajout de 
Domain Name: EXAMPLE.ORG
        8<...>8
URL of the ICANN Whois Inaccuracy Complaint Form: https://www.icann.org/wicf/
----------------------------------------------
{
    "creation_date": "",
    "domain_name": [
        "EXAMPLE.ORG"
    ],
    8<...>8
    "updated_date": ""
}
```

## `110_check_for_name_on_punnycode_replacement.py`
  * À partir d'un domaine indiqué via l'option `-d`.
  * Le script va réaliser un certain nombre de permutations (`a` => `â` par exemple), 
  * Puis tenter de détecter si le domain est réservé & utilisé.
  * La résolution DNS du domaine peut se faire de deux manières différentes (switch via l'option `adapter`) : 
    * `web` pour requêter le service WEB http://dnslookup.fr.
    * `dns` pour réaliser les requêtes DNS via la lib `dnspython`. **Adaptateur par défaut.**
    * `none` quand on se fout des IP et qu'on ne cherche que le WHOIS.
  * Un exemple de résultat : 

```
(VirtualEnv) [user@host corporate_tools]$ ./110_check_for_name_on_punnycode_replacement.py -d sample.fr   
+-----------+--------------------+----------------+----------+----------------+
| Domaine   | Encodage PunnyCode | Encodage UTF-8 | Réservé? |         @IPv4? |
+-----------+--------------------+----------------+----------+----------------+
| sample.fr |          sample.fr |      sample.fr |      Oui | 149.202.133.35 |
| sample.fr |   xn--sampl-rsa.fr |      samplë.fr |      Non |            N/A |
| sample.fr |   xn--sampl-8ra.fr |      samplè.fr |      Non |            N/A |
| sample.fr |   xn--sampl-fsa.fr |      samplé.fr |      Non |            N/A |
|                                     8<...>8                                 |
+-----------+--------------------+----------------+----------+----------------+
```

## `120_check_for_name_completed_by_list.py`
  * À partir d'un domaine et d'une liste de mots.
  * Produit la combinatoire des possibilités.
  * Et en teste l'existence sur tous les TLDs reconnus par l'IANA.
  * Un exemple de résultat : 

```
(VirtualEnv) [user@host corporate_tools]$ ./120_check_for_name_completed_by_list.py -d example.org -wl /tmp/liste
+-----------------------+----------+
| Domaine               | Réservé? |
+-----------------------+----------+
| example-test.africa   |      Non |
| example-test.capetown |      Non |
| example-test.cc       |      Non |
|               8<...>8            |
+-----------------------+----------+
```

## `200_enrich_domains_list.py`
  * À partir d'une liste de noms de domaines.
  * Fait les requêtes WHOIS nécessaires à la récupération de certaines informations.
  * Et produit un fichier CSV.
  * Les expressions régulières permettant de parser le résultat se trouvent dans le module `libs.string.whois_parser`.
  * Un exemple de résultat : 

```
(VirtualEnv) [user@host corporate_tools]$ ./200_enrich_domains_list.py -i /tmp/liste 
Domaine;Registrar;Propriétaire;Date Expiration;DNS
example.org;ICANN;Internet Assigned Numbers Authority;2010-08-30 04:00:00;a.iana-servers.net,b.iana-servers.net
```

# TODO 

| Tâche | Date traitement | 
|-------|-----------------|
| Utiliser le cache pour le traitement `110_check_for_name_on_punnycode_replacement.py` | 2017-12-07 |
| Faire un script qui vient lire le whois de `google` sur chaque TLD connu de l'IANA et en déduit les parsers (car les informations ne changent jamais) | xxxx |
| Revoir la structure du parser pour intégrer le Xème résultat du match de l'expression régulière | xxxx |
| Trouver un moyen de gérer les doubles extensions, comme `.co.uk` ou `.com.br`. | xxxx |
