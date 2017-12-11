"""name_servers : Bancal mais ça peut valoir le coup d'essayer, surtout quand j'aurais fait le TODO pour sélectionner l'index dont j'ai besoin."""
parser = {
  "creation_date": [ "created:\s+(.+)", "" ], 
  "domain_name": [ "DOMAIN NAME:\s+(.+)", "" ], 
  "expiration_date": [ "renewal date:\s+(.+)", "" ], 
  "name_servers": [ "\s{12,}(.+)\. \r\n", "" ],
  "registrant": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ], 
  "registrar": [ "REGISTRAR:\r\n(.+)", "" ], 
  "status": [ None, "CHAMP_ABSENT_DU_RÉFÉRENTIEL" ], 
  "updated_date": [ "last modified:\s+(.+)", "" ]
}
