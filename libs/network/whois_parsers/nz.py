parser = {
  "creation_date": [ "domain_dateregistered: (.+)\+", "" ], 
  "domain_name": [ "domain_name: (.+)", "" ], 
  "expiration_date": [ "domain_datebilleduntil: (.+)\+", "" ], 
  "name_servers": [ "ns_name_[ 0-9 ]{2}: (.+)", "" ], 
  "registrant": [ "registrant_contact_name: (.+)", "" ], 
  "registrar": [ "registrar_name: (.+)", "" ], 
  "status": [ "query_status: (.+)", "" ], 
  "status": [ "ns_name_.+: (.+)", "" ],
  "updated_date": [ "domain_datelastmodified: (.+)\+", "" ]
}
