# Remigiusz Wilk

from datetime import datetime
import time
import random


def timer_dekorator(funkcja):
    def wrapper():
        start = datetime.now()
        funkcja()
        stop = datetime.now()

        czas = stop - start

        komunikat = f'Czas wykonania: {czas}\n'
        print(komunikat)

    return wrapper


@timer_dekorator
def przykladowa_funkcja():
    for _ in range(10):
        print('.', end='', flush=True)
        time.sleep(random.uniform(0, 1))
    print()


if __name__ == '__main__':
    przykladowa_funkcja()
