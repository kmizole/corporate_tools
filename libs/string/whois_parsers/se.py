parser = {
  "creation_date": [ "created:\s+(.+)", "" ], 
  "domain_name": [ "domain:\s+(.+)", "" ], 
  "expiration_date": [ "expires:\s+(.+)", "" ], 
  "name_servers": [ "nserver:\s+(.+)", "" ], 
  "registrant": [ None, "Champ_absent_du_registre" ], 
  "registrar": [ "registrar:\s+(.+)", "" ], 
  "updated_date": [ "modified:\s+(.+)", "" ]
}