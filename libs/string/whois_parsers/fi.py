parser = {
  "creation_date": [ "created\.+:\s+(.+)", "" ], 
  "domain_name": [ "domain\.+:\s+(.+)", "" ], 
  "expiration_date": [ "expires\.+:\s+(.+)", "" ], 
  "name_servers": [ "nserver\.+:\s+(.+) ", "" ], 
  "registrant": [ "name\.+:\s+(.+)", "" ], 
  "registrar": [ "registrar\.+:\s+(.+)", "" ], 
  "status": [ 'status\.+: (.+)', '' ],
  "updated_date": [ "modified\.+:\s+(.*)", "" ]
}
