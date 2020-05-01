import sqlite3

connection = sqlite3.connect('chinook.db')

cursor = connection.cursor()

cursor.execute("SELECT * FROM artists")

print(cursor.fetchall())

#connection.commit()

connection.close()