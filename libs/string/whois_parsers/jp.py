parser = {
  "creation_date": [ "\[ Created on\ ]\s?(.+)", "" ], 
  "domain_name": [ "\[ Domain Name\ ]\s?(.+)", "" ], 
  "expiration_date": [ "\[ Expires on\ ]\s?(.+)", "" ], 
  "name_servers": [ "\[ Name Server\ ]\s*(.+)", "" ], 
  "registrant": [ "\[ Registrant\ ]\s?(.+)", "" ], 
  "registrar": [ None, "" ], 
  "status": [ "\[ Status\ ]\s?(.+)", "" ], 
  "updated_date": [ "\[ Last Updated\ ]\s?(.+)", "" ]
}