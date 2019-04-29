# Remigiusz Wilk
import sqlite3

conn = sqlite3.connect('zaddom09.db')
c = conn.cursor()

zapytanie_sprzet = """
SELECT "nazwa" FROM "plecak" WHERE "rodzaj" LIKE '%sprz%' ORDER BY "nazwa" ASC;
"""


zapytanie_jedzenie = """
SELECT "nazwa" FROM "plecak" WHERE "rodzaj" LIKE '%jedz%' ORDER BY "nazwa" ASC;
"""

zapytanie_waga = """
SELECT "ilosc", "waga" FROM "plecak";
"""

print('Sprzęt:')

c.execute(zapytanie_sprzet)
sprzet = c.fetchall()
# print(produkty)
for s in sprzet:
    print(s[0])

print()

print('Jedzenie:')

c.execute(zapytanie_jedzenie)
jedzenie = c.fetchall()
# print(produkty)
for j in jedzenie:
    print(j[0])

print()

c.execute(zapytanie_waga)
suma = 0
waga = c.fetchall()
# print(waga)

for przedmiot in waga:
    suma_jednego = przedmiot[0] * przedmiot[1]
    suma = suma + suma_jednego

# print(suma)

print(f'Waga zawartości: {suma}g')

conn.close()
