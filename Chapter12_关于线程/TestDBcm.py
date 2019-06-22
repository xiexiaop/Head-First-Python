from DBcm import UseDatabase

dbconfig = {
    'host': '127.0.0.1',
    'user': 'xiezac',
    'password': '1121',
    'database': 'vsearchlogDB'
}

with UseDatabase(dbconfig) as cursor:
    _SQL = """show tables"""
    cursor.execute(_SQL)
    data = cursor.fetchall()
    print(data)
