parser = {
  "creation_date": [ "Registered:\s+(.+)", "" ], 
  "domain_name": [ "Domain:\s+(.+)", "" ], 
  "expiration_date": [ "Expires:\s+(.+)", "" ], 
  "name_servers": [ "Nameserver:\s+(.+)", "" ], 
  "registrant": [ None, "Champ_absent_du_registre" ], 
  "registrar": [ "Registrar:\s+(.+)", "" ], 
  "updated_date": [ None, "1970-01-01T00:00:01" ]
}