# Remigiusz Wilk

from zaddom02_e1 import TaliaKart


def rozdaj_karty(talia, ile_kart=1):
    lista = []

    try:
        for karta in range(ile_kart):

            if ile_kart <= 0:
                return lista

            lista.append(next(talia))

        return lista
    except StopIteration:
        return lista


if __name__ == '__main__':
    talia = TaliaKart()

    gracz1 = rozdaj_karty(talia, 1)
    gracz2 = rozdaj_karty(talia, 1)
    gracz3 = rozdaj_karty(talia, 1)
    gracz4 = rozdaj_karty(talia, 0)

    print(gracz1)
    print(gracz2)
    print(gracz3)
    print(gracz4)
    print(len(gracz1 + gracz2 + gracz3 + gracz4))
