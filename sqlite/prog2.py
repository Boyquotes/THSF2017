import sqlite3

conn = sqlite3.connect('machines.db')

cursor=conn.cursor()
cursor.execute("""
INSERT INTO machines (ip, whatis, mac) VALUES (?,?,?)""", ("192.168.1.1","X260","mac001"))

conn.commit()
