parser = {
  "creation_date": [ ".+Creation Date \(dd/mm/yyyy\):\s+(.+)", "" ], 
  "domain_name": [ ".+Domain Name:\s+(.+)", "" ], 
  "expiration_date": [ ".+Expiration Date \(dd/mm/yyyy\):\s+(.+)", "" ], 
  "name_servers": [ "Nameserver:\s+.+NS\s+(.+)\.", "" ], 
  "registrant": [ ".+Registrant\r\n\s+(.+)", "" ], 
  "registrar": [ "Billing Contact\r\n\s+(.+)", "" ],
  "status": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ],
  "updated_date": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ]
}
