parser = {
  "creation_date": [ "registered: \s?(.+)", "" ], 
  "domain_name": [ "Domain: \s?(.+)", "" ], 
  "expiration_date": [ "expire: \s?(.+)", "" ], 
  "name_servers": [ "nserver: \s*(.+) ", "" ], 
  "registrant": [ "registrant: \s?(.+)", "" ], 
  "registrar": [ "registrar: \s?(.+)", "" ], 
  "status": [ "Status: \s?(.+)", "" ], 
  "updated_date": [ "changed: \s?(.+)", "" ]
}