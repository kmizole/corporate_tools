parser = {
  "creation_date": [ "Registered:\s+(.+)", "" ], 
  "domain_name": [ "Domain:\s+(.+)", "" ], 
  "expiration_date": [ "Expires:\s+(.+)", "" ], 
  "name_servers": [ "Nameserver:\s+(.+)", "" ], 
  "registrant": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ], 
  "registrar": [ "Registrar:\s+(.+)", "" ], 
  "status": [ "Status:\s+(.+)", "" ],
  "updated_date": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ]
}
