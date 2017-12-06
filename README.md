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
