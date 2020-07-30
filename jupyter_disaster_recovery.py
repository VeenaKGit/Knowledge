import sqlite3
from pprint import pprint

connection = sqlite3.connect('history.sqlite')
connection.row_factory = sqlite3.Row  # this is probably required to read each row in a table
cursor = connection.cursor()

# List of all available table
# list_table = cursor.execute('SELECT name from sqlite_master where type= "table"')
# description of table
# des = cursor.execute('pragma table_info("sessions")')
# sql = '''SELECT * FROM sessions LIMIT 10'''
# data = cursor.execute(sql)
# pprint(data.fetchall())

sql = '''SELECT sessions.session, sessions.start, sessions.end, history.source
from sessions
join history on history.session=sessions.session
where start > '2020-03-20'
'''
#1696
data = cursor.execute(sql)
count = 0
with open('output.py', 'w') as f:
    for r in data.fetchall():
        dat = dict(r)['source']
        pprint(count)
        pprint(dat)
        f.write(dat)
        f.write('\n')
        f.write('\n')
        count += 1
pprint(count)
cursor.close()
print("Successful")

