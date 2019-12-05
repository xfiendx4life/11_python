import sqlite3

conn = sqlite3.connect('mtm.db')
cursor = conn.cursor()
with open('create.sql') as f:
	for line in f:
		cursor.execute(line)