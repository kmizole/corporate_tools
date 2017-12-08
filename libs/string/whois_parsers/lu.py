parser = {
  "creation_date": [ "registered:\s+(.+)", "" ], 
  "domain_name": [ "domainname:\s+(.+)", "" ], 
  "expiration_date": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ], 
  "name_servers": [ "nserver:\s+(.+)", "" ], 
  "registrant": [ "org-name:\s+(.+)", "" ], 
  "registrar": [ "registrar-name:\s+(.+)", "" ], 
  "status": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ],
  "updated_date": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ]
}
