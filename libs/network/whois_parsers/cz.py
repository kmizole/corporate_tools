parser = {
  "creation_date": [ "registered: \s?(.+)", "" ], 
  "domain_name": [ "domain:\s+(.+)", "" ], 
  "expiration_date": [ "expire: \s?(.+)", "" ], 
  "name_servers": [ "nserver: \s*(.+) ", "" ], 
  "registrant": [ "registrant: \s?(.+)", "" ], 
  "registrar": [ "registrar: \s?(.+)", "" ], 
  "status": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ], 
  "updated_date": [ "changed: \s?(.+)", "" ]
}
