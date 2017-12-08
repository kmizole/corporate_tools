parser = {
  "creation_date": [ "registration:\s+(.+)", "" ], 
  "domain_name": [ "domain:\s+(.+)", "" ], 
  "expiration_date": [ "renewal:\s+(.+)", "" ], 
  "name_servers": [ "nserver:\s+(.+)", "" ], 
  "registrant": [ "descr:\s+(.+)", "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ], 
  "registrar": [ "person:\s+(.+)", "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ], 
  "status": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ],
  "updated_date": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ]
}
