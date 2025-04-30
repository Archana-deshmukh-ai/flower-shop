import sqlite3

# Path to your old database
old_db_path = 'db.sqlite3'

# Connect
conn = sqlite3.connect(old_db_path)
cursor = conn.cursor()

# List all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in old database:")
for table in tables:
    print(table[0])

conn.close()
