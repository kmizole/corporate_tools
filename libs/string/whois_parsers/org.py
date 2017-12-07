parser = {
    'creation_date': [ r'\nCreated On: \s?(.+)', '' ],
    'domain_name': [ r'Domain Name: \s?(.+)', '' ],
    'expiration_date': [ r'Registry Expiry Date: \s*(.+)', '' ],
    'name_servers': [ r'Name Server: \s?(.+)\s*', '' ],
    'registrant': [ r'Registrant Name: \s*(.+)', '' ],
    'registrar': [ r'Registrar: \s?(.+)', '' ],
    'status': [ r'Status: \s?(.+)', '' ],
    'updated_date': [ r'\nLast Updated On: \s?(.+)', '' ],
}
