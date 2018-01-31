parser = {
  "creation_date": [ "Registered on:\s+(.+)", "" ], 
  "domain_name": [ "Domain name:\n\s+(.+)", "" ], 
  "expiration_date": [ "Expiry date: \s*(.+)", "" ], 
  "name_servers": [ "Name servers:\n\s+((.+\n)+)", "" ], 
  "registrant": [ "Registrant:\n\s+(.+)", "" ], 
  "registrar": [ "Registrar:\n\s+(.+)", "" ], 
  "status": [ "Registration status:\n\s+(.+)", "" ], 
  "updated_date": [ "Last updated:\s+(.+)", "" ]
}
