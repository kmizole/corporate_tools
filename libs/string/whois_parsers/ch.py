parser = {
  "creation_date": [ "First registration date:\n(.+)", "" ], 
  "domain_name": [ "Domain name:\n(.+)", "" ], 
  "expiration_date": [ None, "1970-01-01T00:00:01" ], 
  "name_servers": [ "(.+)\s+\[ [ 0-9\. ]+\ ]", "" ], 
  "registrant": [ "Holder of domain name:\n(.+)", "" ], 
  "registrar": [ "Registrar:\n(.+)", "" ], 
  "updated_date": [ None, "1970-01-01T00:00:01" ]
}