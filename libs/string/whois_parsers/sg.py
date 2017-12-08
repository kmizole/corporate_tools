parser = {
  "creation_date": [ "Creation Date:\s+(.+)", "" ], 
  "domain_name": [ "Domain Name:\s+(.+)", "" ], 
  "expiration_date": [ "Expiration Date:\s+(.+)", "" ], 
  "name_servers": [ None, "IMPOSSIBLE_DE_GARANTIR_AVEC_CERTITUDE_LE_PARSING" ], 
  "registrant": [ "Registrant:\r\n\r\n\s+Name:\s+(.+)", "" ], 
  "registrar": [ "Registrar:\s+(.+)", "" ], 
  "status": [ "Domain Status:\s+(.+)", "" ],
  "updated_date": [ "Modified Date:\s+(.+)", "" ]
}
