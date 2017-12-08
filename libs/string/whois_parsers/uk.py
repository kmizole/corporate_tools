parser = {
  "creation_date": [ "Registered on:\s+(.+)", "" ], 
  "domain_name": [ "Domain name:\r\n\s+(.+)", "" ], 
  "expiration_date": [ "Expiry date: \s*(.+)", "" ], 
  "name_servers": [ None, "IMPOSSIBLE_DE_GARANTIR_AVEC_CERTITUDE_LE_PARSING" ], 
  "registrant": [ "Registrant:\r\n\s+(.+)", "" ], 
  "registrar": [ "Registrar:\r\n\s+(.+)", "" ], 
  "status": [ "Registration status:\r\n\s+(.+)", "" ], 
  "updated_date": [ "Last updated:\s+(.+)", "" ]
}
