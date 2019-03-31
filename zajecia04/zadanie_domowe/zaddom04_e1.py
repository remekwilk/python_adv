# Remigiusz Wilk

from datetime import datetime
import time
import random


def timer(funkcja):
    start = datetime.now()
    funkcja()
    stop = datetime.now()

    czas = stop - start

    komunikat = f'Czas wykonania: {czas}\n'
    print(komunikat)

    return funkcja


def przykladowa_funkcja():
    for _ in range(10):
        print('.', end='', flush=True)
        time.sleep(random.uniform(0, 1))
    print()


if __name__ == '__main__':
    timer(przykladowa_funkcja)
