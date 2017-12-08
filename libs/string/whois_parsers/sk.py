parser = {
  "creation_date": [ "Created:\s+(.+)", "" ], 
  "domain_name": [ "Domain:\s+(.+)", "" ], 
  "expiration_date": [ "Valid Until:\s+(.+)", "" ], 
  "name_servers": [ "Nameserver:\s+(.+)", "" ], 
  "registrant": [ "Registrant:\s+(.+)", "" ], 
  "registrar": [ "Registrar:\s+(.+)", "" ], 
  "status": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ],
  "updated_date": [ "Updated:\s+(.*)$", "" ]
}
