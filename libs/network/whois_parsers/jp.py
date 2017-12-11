parser = {
  "creation_date": [ "\[登録年月日\]\s+(.+)", "" ], 
  "domain_name": [ "\[Domain Name\]\s+(.+)", "" ], 
  "expiration_date": [ "\[有効期限\]\s+(.+)", "" ], 
  "name_servers": [ "\[Name Server\]\s+(.+)", "" ], 
  "registrant": [ "\[Registrant\]\s+(.+)", "" ], 
  "registrar": [ None, "IMPOSSIBLE_DE_GARANTIR_AVEC_CERTITUDE_LE_PARSING" ], 
  "status": [ "\[状態\]\s+(.+)", "" ], 
  "updated_date": [ "\[最終更新\]\s+(.+) ", "" ]
}
