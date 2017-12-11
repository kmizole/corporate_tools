parser = {
  "creation_date": [ "Creation Date:\s+(.+)\r", "" ], 
  "domain_name": [ "Domain Name:\s+(.+)\r", "" ], 
  "expiration_date": [ "Registry Expiry Date:\s+(.+)\r", "" ], 
  "name_servers": [ "Name Server:\s+(.+)\r+", "" ], 
  "registrant": [ "Registrant Name:\s+(.+)\r*", "Champ_absent_du_registre" ], 
  "registrar": [ "Registrar:\s+(.+)\r", "" ], 
  "status": [ "Domain Status: (.+) ", "" ],
  "updated_date": [ "Updated Date:\s+([ 0-9\-:TZ ]+)\r\n", "" ]
}
