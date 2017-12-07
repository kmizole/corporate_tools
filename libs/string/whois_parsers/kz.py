parser = {
  "creation_date": [ "Domain created:\s+(.+)\s+.*$", "" ], 
  "domain_name": [ "Domain Name:\s+(.+)", "" ], 
  "expiration_date": [ None, "" ], 
  "name_servers": [ "^.+server\.+:\s+(.+)", "" ], 
  "registrant": [ "Name\.+:\s+(.+)", "" ], 
  "registrar": [ "Current Registrar:\s+(.+)", "" ], 
  "updated_date": [ "Last modified:\s+(.*)\s+.*$", "" ]
}