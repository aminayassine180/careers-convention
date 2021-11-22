#!/usr/bin/env python3

# local imports
import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

conn.execute("CREATE TABLE delegates (id INTEGER PRIMARY KEY, name TEXT, location TEXT, description TEXT, category TEXT, internalurl TEXT, externalurl TEXT)")
print("Table created successfully")
conn.close()

