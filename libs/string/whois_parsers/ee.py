parser = {
  "creation_date": [ "registered:\s+(.+)\s+\+.*", "" ], 
  "domain_name": [ "Domain:\s*\nname:\s+(.+)", "" ], 
  "expiration_date": [ "expire:\s+(.+)", "" ], 
  "name_servers": [ "nserver:\s+(.+)", "" ], 
  "registrant": [ "Registrant:\nname:\s+(.+)", "" ], 
  "registrar": [ "Registrar:\nname:\s+(.+)", "" ], 
  "status": [ "status:\s+(.+)", "" ],
  "updated_date": [ "changed:\s+(.*)\s+\+.*", "" ]
}
