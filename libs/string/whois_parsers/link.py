parser = {
  "creation_date": [ "Creation Date: (.+).[0-9]{3}Z", "" ], 
  "domain_name": [ "Domain Name: (.+)", "" ], 
  "expiration_date": [ "Registry Expiry Date: (.+)", "" ], 
  "name_servers": [ "Name Server: (.+)", "" ], 
  "registrant": [ "Registrant Organization: (.+)", "" ], 
  "registrar": [ "Registrar: (.+)", "" ], 
  "status": [ "Status: (.+) ", "" ], 
  "updated_date": [ "Updated Date: (.+).[0-9]{3}Z", "" ]
}
