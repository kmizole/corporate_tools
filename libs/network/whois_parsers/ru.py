parser = {
  "creation_date": [ "created:\s+(.+)", "" ], 
  "domain_name": [ "domain:\s+(.+)", "" ], 
  "expiration_date": [ "paid-till:\s+(.+)", "" ], 
  "name_servers": [ "nserver:\s+(.+)", "" ], 
  "registrant": [ "org:\s+(.+)", "" ],
  "registrar": [ "registrar:\s+(.+)", "" ], 
  "status": [ "state:\s+(.+)", "" ], 
  "updated_date": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ]
}
