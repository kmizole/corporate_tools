parser = {
  "creation_date": [ "Registered on: \s*(.+)", "" ], 
  "domain_name": [ "Domain Name: \s?(.+)", "" ], 
  "expiration_date": [ "Expiry Date: \s*(.+)", "" ], 
  "name_servers": [ "Name Servers: \s*(.+)\s*", "" ], 
  "registrant": [ "Registrant: \n\s*(.+)", "" ], 
  "registrar": [ "Registrar: \s?(.+)", "" ], 
  "status": [ "Registration status: \n\s*(.+)", "" ], 
  "updated_date": [ "Last updated: \s*(.+)", "" ]
}