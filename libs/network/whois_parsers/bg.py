parser = {
  "creation_date": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ],
  "domain_name": [ "DOMAIN NAME:\s+(.+)", "" ], 
  "expiration_date": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ], 
  "name_servers": [ None, "IMPOSSIBLE_DE_GARANTIR_AVEC_CERTITUDE_LE_PARSING" ],
  "registrant": [ "REGISTRANT:\n(.+)", "" ], 
  "registrar": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ], 
  "status": [ 'registration status: (.+)', '' ],
  "updated_date": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ],
}
