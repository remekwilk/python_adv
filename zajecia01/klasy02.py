class Kot:
    _lapy = 4

    def __init__(self, imie):
        self.imie = imie

    def __repr__(self):         # zawsze tworzyc (__rept__) (__str__)jest bardziej dodatkowy
        return f'Kot {self.imie}' #(__str__ )dziala tak samo jak (__repr__)

    def daj_glos(self):
        print("Miau!")


if __name__ == '__main__':
    k = Kot('Filemon')
    print(k)
    k.daj_glos()

    # print(str(k))
