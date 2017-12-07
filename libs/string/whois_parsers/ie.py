parser = {
  "creation_date": [ "registration:\s+(.+)", "" ], 
  "domain_name": [ "domain:\s+(.+)", "" ], 
  "expiration_date": [ "renewal:\s+(.+)", "" ], 
  "name_servers": [ "nserver:\s+(.+)", "" ], 
  "registrant": [ None, "Champ_absent_du_registre" ], 
  "registrar": [ None, "Champ_absent_du_registre" ], 
  "updated_date": [ None, "1970-01-01T00:00:01" ]
}