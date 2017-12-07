parser = {
  "creation_date": [ "Registered: \s*(.+)\n", "" ], 
  "domain_name": [ "\nDomain: \s*(.+)", "" ], 
  "expiration_date": [ "Expiry Date: \s*(.+)", "" ], 
  "name_servers": [ "\nnameservers: \s*(.+)\n\s*(.+)\n", "" ], 
  "registrant": [ "Registrant: \s*\n\s*(.+)", "" ], 
  "registrar": [ "Registrar Technical Contacts: \s*\n\s*Name.*\n\sOrganisation: \s*(.+)", "" ], 
  "status": [ "Status: \s?(.+)", "" ], 
  "updated_date": [ "\nlast modified: \s*(.+)\n", "" ]
}