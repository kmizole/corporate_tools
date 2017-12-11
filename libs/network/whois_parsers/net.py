parser = {
  "creation_date": [ "Creation Date: \s?(.+)", "" ], 
  "domain_name": [ "Domain Name: \s?(.+)", "" ], 
  "expiration_date": [ "Registry Expiry Date: (.+)", "" ], 
  "name_servers": [ "Name Server: \s*(.+)\s*", "" ], 
  "registrant": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ], 
  "registrar": [ "Registrar: \s?(.+)", "" ], 
  "status": [ "Domain Status: (.+) ", "" ], 
  "updated_date": [ "Updated Date: \s?(.+)", "" ]
}
