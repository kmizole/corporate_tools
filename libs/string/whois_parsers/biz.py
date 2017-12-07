parser = {
  "creation_date": [ "Domain Registration Date: \s?(.+)", "" ], 
  "domain_name": [ "Domain Name: \s?(.+)", "" ], 
  "expiration_date": [ "Domain Expiration Date: \s?(.+)", "" ], 
  "name_servers": [ "Name Server: \s*(.+)\s*", "" ], 
  "registrant": [ "Registrant Organization: \s?(.+)", "" ], 
  "registrar": [ "Registrar: \s?(.+)", "" ], 
  "status": [ None, "" ], 
  "updated_date": [ "Domain Last Updated Date: \s?(.+)", "" ]
}