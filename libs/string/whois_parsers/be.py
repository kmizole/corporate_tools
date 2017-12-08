parser = {
  "creation_date": [ "Registered:\s+(.+)", "" ], 
  "domain_name": [ "Domain:\s+(.+)", "" ], 
  "expiration_date": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ],
  "name_servers": [ "Nameservers:\n\s+(.+)", "IMPOSSIBLE_DE_GARANTIR_AVEC_CERTITUDE_LE_PARSING" ], 
  "registrant": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ], 
  "registrar": [ "Registrar:\s+\n\s+Name:\s+(.+)", "" ], 
  "status": [ "Status:\s+(.+)", "" ], 
  "updated_date": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ]
}
