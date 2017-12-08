parser = {
  "creation_date": [ "created:\s+(.+)", "" ], 
  "domain_name": [ "domain:\s+(.+)", "" ], 
  "expiration_date": [ "expires:\s+(.+)", "" ], 
  "name_servers": [ "nserver:\s+(.+)", "" ], 
  "registrant": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ], 
  "registrar": [ "registrar:\s+(.+)", "" ], 
  "updated_date": [ "modified:\s+(.+)", "" ]
}
