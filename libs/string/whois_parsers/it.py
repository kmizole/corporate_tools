parser = {
  "creation_date": [ "Created: \s?(.+)", "" ], 
  "domain_name": [ "Domain: \s?(.+)", "" ], 
  "expiration_date": [ "Expire Date: \s?(.+)", "" ], 
  "name_servers": [ "Nameservers: \s?(.+)\s?(.+)\s?(.+)\s?(.+)", "" ], 
  "registrant": [ "Registrant: \s?Name: \s?(.+)", "" ], 
  "registrar": [ "Registrar: \s*Organization: \s*(.+)", "" ], 
  "status": [ "Status: \s?(.+)", "" ], 
  "updated_date": [ "Last Update: \s?(.+)", "" ]
}