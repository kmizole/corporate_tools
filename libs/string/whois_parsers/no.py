parser = {
  "creation_date": [ "Created:\s+(.+)", "" ], 
  "domain_name": [ "Domain Name\.+:\s+(.+)", "" ], 
  "expiration_date": [ None, "1970-01-01T00:00:01" ], 
  "name_servers": [ "Name Server Handle\.+:\s+(.+)", "" ], 
  "registrant": [ "Legal-c Handle\.+:\s+(.+)", "" ], 
  "registrar": [ "Registrar Handle\.+:\s+(.+)", "" ], 
  "updated_date": [ "Last updated:\s+(.+)", "" ]
}