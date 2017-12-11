parser = {
  "creation_date": [ "Creation Date:\s+(.+)", "" ], 
  "domain_name": [ "Domain Name:\s+(.+)", "" ], 
  "expiration_date": [ "Registry Expiry Date:\s+(.+)", "" ], 
  "name_servers": [ "Name Server:\s+(.+)", "" ], 
  "registrant": [ "Registrant Organization:\s+(.+)", "" ], 
  "registrar": [ "Registrar:\s+(.+)", "" ],
  "status": [ "Domain Status: (.+) ", "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ],
  "updated_date": [ "Updated Date:\s+(.+)", "" ]
}
