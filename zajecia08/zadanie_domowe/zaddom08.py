# Remigiusz Wilk
from wc_funkcje import ustaw_logger, wc
import logging
import datetime
import argparse

if __name__ == '__main__':
    start = datetime.datetime.now()

    # tutaj należy napisać kod odpowiedzialny za wczytanie argumentów
    parser = argparse.ArgumentParser(description='WORD COUNTER')
    parser.add_argument('-l', '--loglevel',choices=logging._nameToLevel,
                        default=logging.WARNING, help='Ustawia poziom logowania')
    parser.add_argument('plik', help='Nazwa pliku do analizy')

    args = parser.parse_args()

    nazwa_pliku = args.plik

    wybrany_szablon = 'pelny'
    poziom_logowania = args.loglevel

    ustaw_logger(poziom_logowania)
    wynik = wc(nazwa_pliku, wybrany_szablon)


    print(wynik)

    czas_wykonania = datetime.datetime.now() - start
    logging.debug(f'czas wykonywania programu: {czas_wykonania}')
