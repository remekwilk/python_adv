class Kot:
    _lapy = 4

    def __init__(self, imie):
        self.imie = imie

    def daj_glos(self):
        print("Miau!")


if __name__ == '__main__':
    k = Kot('Filemon')
    print(k)
    k.daj_glos()

    # print(k.__dir__())
