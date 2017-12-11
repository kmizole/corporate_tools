parser = {
  "creation_date": [ "created:\s+(.+)\s+#.*", "" ], 
  "domain_name": [ "domain:\s+(.+)", "" ], 
  "expiration_date": [ "expires:\s+(.+)", "" ], 
  "name_servers": [ "nserver:\s+(.+)", "" ], 
  "registrant": [ "owner:\s+(.+)", "" ], 
  "registrar": [ "owner:\s+(.+)", "" ], 
  "updated_date": [ "changed:\s+(.*)$", "" ]
}