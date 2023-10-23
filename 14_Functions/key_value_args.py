# To receive named arguments as a dictionary we use ** before the param name

def listTerms(**terms):
    # In this case terms is a dictionary
    for key, value in terms.items():
        print(f'{key}: {value}')


listTerms(IDE='Integrated Development Environment', PK='Primary Key')
listTerms(DBMS='Database Management System')
