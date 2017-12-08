parser = {
  "creation_date": [ "Domain created:\s+(.+) ", "" ], 
  "domain_name": [ "Domain Name\.+: (.+)", "" ], 
  "expiration_date": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ], 
  "name_servers": [ ".+ server\.+:\s+(.+)", "" ], 
  "registrant": [ "Organization Using Domain Name\nName\.+:\s+(.+)", "" ], 
  "registrar": [ "Current Registar: (.+)", "" ], 
  "status": [ "Domain status : ([a-z]+)", "" ],
  "updated_date": [ "Last modified :\s+(.*) \(", "" ]
}
