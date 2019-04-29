# Remigiusz Wilk
import sqlite3
import string
conn = sqlite3.connect('zaddom09.db')
c = conn.cursor()

while True:
    nazwa = input('Podaj nazwę przedmiotu: ').capitalize()
    if nazwa.isalpha():
        break
    else:
        print('Błędna nazwa!!! Nazwa bez cyfr i znakow specjalnych')
        continue
while True:
    try:
        ilosc = int(input(f'Ile {nazwa} dołożyć do plecaka: '))
        waga = float(input(f'Waga jednej sztuki {nazwa}: '))
        break
    except ValueError:
        print('Błędna wartość!!')
        continue

while True:
    rodzaj = input('[s]przet czy [j]edzenie? ').lower()
    if rodzaj == 's' or rodzaj == 'sprzet':
        rodzaj = 'sprzet'
        break
    elif rodzaj == 'j' or rodzaj == 'jedzenie':
        rodzaj = 'jedzenie'
        break
    else:
        print('Błędna wartość!')
        continue


# tutaj stwórz i wykonaj zapytanie do bazy
zapytanie = """
INSERT INTO 'plecak'
VALUES (NULL, ?, ?, ?, ?);
"""
c.execute(zapytanie, (nazwa, rodzaj, ilosc, waga))

conn.commit()
conn.close()
