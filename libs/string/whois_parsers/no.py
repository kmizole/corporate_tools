parser = {
  "creation_date": [ "Created:\s+(.+)", "" ], 
  "domain_name": [ "Domain Name\.+:\s+(.+)", "" ], 
  "expiration_date": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ], 
  "name_servers": [ "Name Server Handle\.+:\s+(.+)", "" ], 
  "registrant": [ "Legal-c Handle\.+:\s+(.+)", "" ], 
  "registrar": [ "Registrar Handle\.+:\s+(.+)", "" ], 
  "status": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ],
  "updated_date": [ "Last updated:\s+(.+)", "" ]
}
