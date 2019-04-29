import logging


def policz_linie(s):
    return len(s.split('\n'))


def policz_wyrazy(s):
    return sum([len(x.split()) for x in s.split('\n')])


def policz_bajty(s):
    return len(s.encode())


def ustaw_logger(poziom_logowania):
    format = '%(levelname)s [%(asctime)s] - %(message)s'
    logging.basicConfig(format=format, level=poziom_logowania)


def wc(nazwa_pliku, wybrany_szablon):
    try:
        with open(nazwa_pliku) as f:
            logging.info(f'otwarto plik {nazwa_pliku}')
            zawartosc = f.read()
    except FileNotFoundError:
        logging.warning(f'nie znaleziono pliku {nazwa_pliku}')
        exit()

    szablony = {'pelny': '{linie} {wyrazy} {bajty} {nazwa_pliku}',
                'linie': '{linie} {nazwa_pliku}'}

    logging.info('wybrano szablon pełny')
    szablon = szablony[wybrany_szablon]

    wynik = szablon.format(linie=policz_linie(zawartosc),
                           wyrazy=policz_wyrazy(zawartosc),
                           bajty=policz_bajty(zawartosc),
                           nazwa_pliku=nazwa_pliku)

    return wynik
