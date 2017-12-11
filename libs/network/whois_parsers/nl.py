parser = {
  "creation_date": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ], 
  "domain_name": [ "Domain name: (.+)", "" ], 
  "expiration_date": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ], 
  "name_servers": [ None, "IMPOSSIBLE_DE_GARANTIR_AVEC_CERTITUDE_LE_PARSING" ], 
  "registrant": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ], 
  "registrar": [ "Registrar:\r\n\s+(.+)\n", "" ], 
  "status": [ "Status:\s+(.+)", "" ],
  "updated_date": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ]
}
