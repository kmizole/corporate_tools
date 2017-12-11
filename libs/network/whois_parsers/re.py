parser = {
  "creation_date": [ "created: \s?(.+)", "" ], 
  "domain_name": [ "domain: \s?(.+)", "" ], 
  "expiration_date": [ "Expiry Date: \s?(.+)", "" ], 
  "name_servers": [ "nserver: \s*(.+)", "" ], 
  "registrant": [ "contact: \s*(.+)", "" ], 
  "registrar": [ "registrar: \s*(.+)", "" ], 
  "status": [ "status: \s?(.+)", "" ], 
  "updated_date": [ "last-update: \s?(.+)", "" ]
}