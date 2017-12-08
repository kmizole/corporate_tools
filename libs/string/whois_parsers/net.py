parser = {
  "creation_date": [ "Creation Date: \s?(.+)", "" ], 
  "domain_name": [ "Domain Name: \s?(.+)", "" ], 
  "expiration_date": [ "Registry Expiry Date: (.+)", "" ], 
  "name_servers": [ "Name Server: \s*(.+)\s*", "" ], 
  "registrant": [ "Registrant Name: (.+)", "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ], 
  "registrar": [ "Registrar: \s?(.+)", "" ], 
  "status": [ "^\s+Status: \s?(.+)", "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ], 
  "updated_date": [ "Updated Date: \s?(.+)", "" ]
}
