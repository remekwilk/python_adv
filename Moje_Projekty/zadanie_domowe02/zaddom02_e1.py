# Remigiusz Wilk
import random

class TaliaKart:
    def __init__(self):
        self._karty = ['2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠', '2♣', '3♣', '4♣',
                       '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥',
                       '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦',
                       'J♦', 'Q♦', 'K♦', 'A♦']

    def __next__(self):
        if (len(self._karty)) == 0:
            raise StopIteration

        karta = random.choice(self._karty)
        self._karty.remove(karta)

        return karta


    def __iter__(self):
        return self


if __name__ == '__main__':
    talia = TaliaKart()
    # print(list(talia))
    # print(next(talia))
    for karta in talia:
       print(list(karta))