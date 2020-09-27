import fdb
import pyodbc
import os
import import_env_file

# FIREBIRD CONNECT

con = fdb.connect(database=os.getenv('FDB_DATABASE'), user=os.getenv('FDB_USERNAME'), password=os.getenv('FDB_PASSWORD'))
cur = con.cursor()

# first file
cur.execute("select id, first_name from table_first_names order by id")
first_names = cur.fetchall()

if os.path.exists("first_names.txt"):
    print("file first_names already exists!")
    exit(1)

f1 = open("first_names.txt", "w")
for first_name in first_names:
    f1.write(str(first_name[0]) + ", " + first_name[1] + "\n")
f1.close()

# second file
cur.execute("select id, last_name from table_last_names order by id")
last_names = cur.fetchall()

if os.path.exists("last_names.txt"):
    print("file last_names already exists!")
    exit(1)

f2 = open("last_names.txt", "w")
for last_name in last_names:
    f2.write(str(last_name[0]) + ", " + last_name[1] + "\n")
f2.close()

con.close()

# READING FILES

first_names = {}
with open('first_names.txt', 'r') as f:
    line = f.readline()
    while line:
        line = line.rstrip('\n').replace(' ', '')
        el = line.split(',')
        first_names[el[0]] = el[1]
        line = f.readline()

last_names = {}
with open('last_names.txt', 'r') as f:
    line = f.readline()
    while line:
        line = line.rstrip('\n').replace(' ', '')
        el = line.split(',')
        last_names[el[0]] = el[1]
        line = f.readline()


# MSSQL

cnxn = pyodbc.connect('DRIVER={0};SERVER={1};PORT={2};DATABASE={3};UID={4};PWD={5}'.format(os.getenv('MSSQL_DRIVER'),
                                                                                             os.getenv('MSSQL_HOST'),
                                                                                             os.getenv('MSSQL_PORT'),
                                                                                             os.getenv('MSSQL_DB'),
                                                                                             os.getenv('MSSQL_USERNAME'),
                                                                                             os.getenv('MSSQL_PASSWORD')))

cursor = cnxn.cursor()
for i in first_names:
    cursor.execute("INSERT INTO schema_test.people (id, first_name, last_name) VALUES (?, ?, ?);", [i, first_names[i], last_names[i]])
cnxn.commit()
cursor.close()

print('success!')
