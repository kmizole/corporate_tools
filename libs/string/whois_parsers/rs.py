parser = {
  "creation_date": [ "Registration Date:\s+(.+)", "" ], 
  "domain_name": [ "Domain name:\s+(.+)", "" ], 
  "expiration_date": [ "Expiration Date:\s+(.+)", "" ], 
  "name_servers": [ "DNS:\s+(.+) - [ 0-9. ]+", "" ], 
  "registrant": [ "Registrant:\s+(.+)", "" ], 
  "registrar": [ "Registrar:\s+(.+)", "" ], 
  "updated_date": [ "Modification Date:\s+(.+)", "" ]
}