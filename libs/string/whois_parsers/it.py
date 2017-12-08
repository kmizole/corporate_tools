parser = {
  "creation_date": [ "Created:\s+(.+)", "" ], 
  "domain_name": [ "Domain:\s+(.+)", "" ], 
  "expiration_date": [ "Expire Date:\s+(.+)", "" ], 
  "name_servers": [ None, "IMPOSSIBLE_DE_GARANTIR_AVEC_CERTITUDE_LE_PARSING" ], 
  "registrant": [ "Registrant\n\s+Organization:\s+(.+)", "" ], 
  "registrar": [ "Registrar\n\s+Organization:\s+(.+)", "" ], 
  "status": [ "Status:\s+(.+)", "" ], 
  "updated_date": [ "Last Update:\s+(.+)", "" ]
}
