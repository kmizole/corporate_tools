parser = {
  "creation_date": [ "Creation Date: (.+)", "" ], 
  "domain_name": [ "Domain Name: (.+)", "" ], 
  "expiration_date": [ "Registry Expiry Date: \s*(.+)", "" ], 
  "name_servers": [ "Name Server: (.+)\s*", "" ], 
  "registrant": [ "Registrant Organization: \s*(.+)", "" ], 
  "registrar": [ "Registrar: (.+)", "" ], 
  "status": [ "Status: (.+) ", "" ], 
  "updated_date": [ "Updated Date: (.+)", "" ]
}
