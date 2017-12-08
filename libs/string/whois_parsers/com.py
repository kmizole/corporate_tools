parser = {
  "creation_date": [ "Creation Date: \s?(.+)", "" ], 
  "domain_name": [ "Domain Name: \s?(.+)", "" ], 
  "expiration_date": [ "Registry Expiry Date: \s?(.+)", "" ], 
  "name_servers": [ "Name Server: \s*(.+)\s*", "" ], 
  "registrant": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ], 
  "registrar": [ "Registrar: \s?(.+)", "" ], 
  "status": [ "Status: \s?(.+)", "" ], 
  "updated_date": [ "Updated Date: \s?(.+)", "" ]
}
