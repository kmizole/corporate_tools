parser = {
  "creation_date": [ "created:\s+(.+)", "" ], 
  "domain_name": [ "domain:\s+(.+)", "" ], 
  "expiration_date": [ "expire:\s+(.+)", "" ], 
  "name_servers": [ "nameserver:\s+(.+)", "" ], 
  "registrant": [ "registrant:\s+(.+)", "" ], 
  "registrar": [ "registrar:\s+(.+)", "" ], 
  "updated_date": [ None, "1970-01-01T00:00:01" ]
}