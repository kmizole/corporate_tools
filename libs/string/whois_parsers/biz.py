parser = {
  "creation_date": [ "Creation Date: (.+)", "" ], 
  "domain_name": [ "Domain Name: \s?(.+)", "" ], 
  "expiration_date": [ "Registry Expiry Date: (.+)", "" ], 
  "name_servers": [ "Name Server: (.+)", "" ], 
  "registrant": [ "Registrant Organization: \s?(.+)", "" ], 
  "registrar": [ "Registrar: \s?(.+)", "" ], 
  "status": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ], 
  "updated_date": [ "Updated Date: \s?(.+)", "" ]
}
