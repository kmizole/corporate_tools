parser = {
  "creation_date": [ "created:\s+(.+)", "" ], 
  "domain_name": [ "domain:\s+(.+)", "" ], 
  "expiration_date": [ "expire:\s+(.+)", "" ], 
  "name_servers": [ "nameserver:\s+(.+)", "" ], 
  "registrant": [ "registrant:\s+(.+)", "" ], 
  "registrar": [ "registrar:\s+(.+)", "" ], 
  "status": [ "status:\t+(.+)", "" ],
  "updated_date": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ]
}
