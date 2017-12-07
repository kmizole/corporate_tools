parser = {
  "creation_date": [ "Registered: \s*(.+)\n", "" ], 
  "domain_name": [ "\ndomain: \s*(.+)", "" ], 
  "expiration_date": [ "\npaid-till: \s*(.+)", "" ], 
  "name_servers": [ "\nnserver: \s*(.+)", "" ], 
  "registrant": [ "Registrant Name: \s*(.+)", "" ], 
  "registrar": [ "Registrar: \s?(.+)", "" ], 
  "status": [ "Status: \s?(.+)", "" ], 
  "updated_date": [ "Changed: \s*(.+)\n", "" ]
}