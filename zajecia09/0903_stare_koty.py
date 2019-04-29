import sqlite3

conn = sqlite3.connect('zadanie09_baza.db')

c = conn.cursor()

zapytanie = """
SELECT * FROM 'zwierzaki' WHERE wiek > 7;
"""
c.execute(zapytanie)

for zwierzak in c:
    print(zwierzak)
conn.close()
