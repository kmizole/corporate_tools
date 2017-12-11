parser = {
  "creation_date": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ], 
  "domain_name": [ "Domain: \s*(.+)", "" ], 
  "expiration_date": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ], 
  "name_servers": [ "Nserver: (.+)", "" ], 
  "registrant": [ "\[Holder]\nType:.+\nName: (.+)", "" ], 
  "registrar": [ "\[Registrar]\nType:.+\nName: (.+)", "" ], 
  "status": [ "Status: (.+)", "" ], 
  "updated_date": [ "Updated: (.+)\.", "" ]
}
