import pypyodbc

cnxn = pypyodbc.connect("Driver={SQL Server};"
                        "Server=localhost;"
                        "Database=bs-mssql-linux;"
                        "uid=sa;pwd=Password1")

cursor = cnxn.cursor()
cursor.execute('SELECT * FROM Products')

for row in cursor:
    print('row = %r' % (row,))
