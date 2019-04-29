import sqlite3

conn = sqlite3.connect('zadanie09_baza.db')

c = conn.cursor()

zapytanie = """

INSERT INTO 'zwierzaki' ('imie', 'gatunek', 'wiek') 
VALUES 
    ('Filemon', 'kot', 0.5),
    ('Bonifacy', 'kot', 12),
    ('Reksio', 'pies', 3),
    ('Garfield', 'kot', 8),
    ('Pluto', 'pies', 5);
"""
c.execute(zapytanie)

conn.commit()
conn.close()
