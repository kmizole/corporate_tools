parser = {
  "creation_date": [ "Registered On:\s+(.+)", "" ], 
  "domain_name": [ "Domain Name:\s+(.+)", "" ], 
  "expiration_date": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL"], 
  "name_servers": [ "Nameserver:\s+(.+)", "" ], 
  "registrant": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ], 
  "registrar": [ "Registrar:\s+(.+)", "" ], 
  "status": [ "\s+Domain Status: (.+)", "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ],
  "updated_date": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ]
}
