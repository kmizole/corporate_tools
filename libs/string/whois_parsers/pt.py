parser = {
  "creation_date": [ ".+Creation Date \(dd/mm/yyyy\):\s+(.+)", "" ], 
  "domain_name": [ ".+Domain Name:\s+(.+)", "" ], 
  "expiration_date": [ ".+Expiration Date \(dd/mm/yyyy\):\s+(.+)", "" ], 
  "name_servers": [ ".+Nameserver:\s+.+NS\s+(.+)\.", "" ], 
  "registrant": [ ".+Registrant\n\s+(.+)", "TODO" ], 
  "registrar": [ None, "Champ_absent_du_registre" ], 
  "updated_date": [ None, "1970-01-01T00:00:01" ]
}