parser = {
  "creation_date": [ "\ncreated: \s*(.+)\n", "" ], 
  "domain_name": [ "Domain Name: \s?(.+)", "" ], 
  "expiration_date": [ "Expiry Date: \s*(.+)", "" ], 
  "name_servers": [ "\nnameservers: \s*(.+)\n\s*(.+)\n", "" ], 
  "registrant": [ "Registrant: \n\s*(.+)", "" ], 
  "registrar": [ "Registrar: \s?(.+)", "" ], 
  "status": [ "\nStatus: \n\s*(.+)", "" ], 
  "updated_date": [ "\nlast modified: \s*(.+)\n", "" ]
}