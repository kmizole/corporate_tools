parser = {
  "creation_date": [ "domain_dateregistered: \s?(.+)", "" ], 
  "domain_name": [ "domain_name: \s?(.+)", "" ], 
  "expiration_date": [ "domain_datebilleduntil: \s?(.+)", "" ], 
  "name_servers": [ "ns_name_[ 0-9 ]{2}: \s?(.+)", "" ], 
  "registrant": [ "registrant_contact_name: \s?(.+)", "" ], 
  "registrar": [ "registrar_name: \s?(.+)", "" ], 
  "status": [ "query_status: \s?(.+)", "" ], 
  "updated_date": [ "domain_datelastmodified: \s?(.+)", "" ]
}