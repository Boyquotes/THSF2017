import sqlite3

conn = sqlite3.connect('machines.db')

cursor=conn.cursor()
cursor.execute("""

CREATE TABLE machines (
id_machines INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
ip TEXT,
whatis TEXT,
mac TEXT
)
""")

conn.commit()
