parser = {
  "creation_date": [ "registered:\s+(.+)", "" ], 
  "domain_name": [ "domainname:\s+(.+)", "" ], 
  "expiration_date": [ None, "1970-01-01T00:00:01" ], 
  "name_servers": [ "nserver:\s+(.+)", "" ], 
  "registrant": [ "org-name:\s+(.+)", "" ], 
  "registrar": [ "registrar-name:\s+(.+)", "" ], 
  "updated_date": [ None, "1970-01-01T00:00:01" ]
}