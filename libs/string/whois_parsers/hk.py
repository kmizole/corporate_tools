parser = {
  "creation_date": [ "Domain Name Commencement Date:\s+(.+)", "" ], 
  "domain_name": [ "Domain Name:\s+(.+)", "" ], 
  "expiration_date": [ "Expiry Date:\s+(.+)", "" ], 
  "name_servers": [ None, "IMPOSSIBLE_DE_GARANTIR_AVEC_CERTITUDE_LE_PARSING" ],
  "registrant": [ "Registrant Contact Information:\n\nCompany English Name .+:\s+(.+)", "" ], 
  "registrar": [ "Registrar Name:\s+(.+)", "" ], 
  "status": [ "Domain Status: (.+)", "" ],
  "updated_date": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ]
}
