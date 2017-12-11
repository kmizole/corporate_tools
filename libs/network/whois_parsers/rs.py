parser = {
  "creation_date": [ "Registration date: (.+)", "" ], 
  "domain_name": [ "Domain name: (.+)", "" ], 
  "expiration_date": [ "Expiration date:+(.+)", "" ], 
  "name_servers": [ "DNS:\s+(.+) - ", "" ], 
  "registrant": [ "Registrant:\s+(.+)", "" ], 
  "registrar": [ "Registrar:\s+(.+)", "" ], 
  "status": [ "Domain status: (.+)", "" ],
  "updated_date": [ "Modification date: (.+)", "" ]
}
