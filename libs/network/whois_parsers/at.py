parser = {
  "creation_date": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ], 
  "domain_name": [ "domain: \s?(.+)", "" ], 
  "expiration_date": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ], 
  "name_servers": [ "nserver: \s*(.+)", "" ], 
  "registrant": [ "organization: \s*(.+)", "" ], 
  "registrar": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ], 
  "status": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ], 
  "updated_date": [ "changed: \s?(.+)", "" ]
}
