parser = {
  "creation_date": [ "\ncreated: \s*(.+)", "" ], 
  "domain_name": [ "\ndomain: \s*(.+)", "" ], 
  "expiration_date": [ "\npaid-till: \s*(.+)", "" ], 
  "name_servers": [ "\nnserver: \s*(.+)", "" ], 
  "registrant": [ "Registrant Name: \s*(.+)", "" ], 
  "registrar": [ "Registrar: \s?(.+)", "" ], 
  "status": [ "\nstate: \s*(.+)", "" ], 
  "updated_date": [ "Updated Date: \s?(.+)", "" ]
}