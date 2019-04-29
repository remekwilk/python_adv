from zadanie08_funkcje import policz_linie, policz_wyrazy, policz_bajty
import logging
import datetime
format = '%(levelname)s [%(asctime)s] - %(message)s'
datefmt = '%Y-%m-%d %H:%M:%S'

start = datetime.datetime.now()

logging.basicConfig(level=logging.DEBUG, format=format, datefmt=datefmt)


nazwa_pliku = 'zen.txt'

try:
    with open(nazwa_pliku) as f:
        zawartosc = f.read()
except FileNotFoundError:
    logging.error(f'Przerwanie pracy z powodu braku pliku')
    exit()
logging.info('Wczytano plik zen.txt')

szablony = {'pelny': '{linie} {wyrazy} {bajty} {nazwa_pliku}',
            'linie': '{linie} {nazwa_pliku}'}

logging.info('Wybrano szablon "pelny"')

szablon = szablony['pelny']

wynik_pelny = szablon.format(linie=policz_linie(zawartosc),
                             wyrazy=policz_wyrazy(zawartosc),
                             bajty=policz_bajty(zawartosc),
                             nazwa_pliku=nazwa_pliku)

czas_od_startu = datetime.datetime.now() - start

print(wynik_pelny)

logging.debug(f'Czas wykonania skryptu: {czas_od_startu}')