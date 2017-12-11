parser = {
  "creation_date": [ "\[ Registered Date\ ]\s?(.+)", "" ], 
  "domain_name": [ "\[ Domain Name\ ]\s?(.+)", "" ], 
  "expiration_date": [ "\[ State\ ].+\((.+)\)", "" ], 
  "name_servers": [ "\[ Name Server\ ]\s*(.+)", "" ], 
  "registrant": [ "\[ Registrant\ ]\s?(.+)", "" ], 
  "registrar": [ None, "" ], 
  "status": [ "\[ Status\ ]\s?(.+)", "" ], 
  "updated_date": [ "\[ Last Update\ ]\s?(.+)", "" ]
}