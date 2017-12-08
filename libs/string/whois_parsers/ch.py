parser = {
  "creation_date": [ "First registration date:\n(.+)", "" ], 
  "domain_name": [ "Domain name:\n(.+)", "" ], 
  "expiration_date": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ], 
  "name_servers": [ "(.+)\s+\[ [ 0-9\. ]+\ ]", "IMPOSSIBLE_DE_GARANTIR_AVEC_CERTITUDE_LE_PARSING" ], 
  "registrant": [ "Holder of domain name:\n(.+)", "" ], 
  "registrar": [ "Registrar:\n(.+)", "" ], 
  "status": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ],
  "updated_date": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ]
}
