# Remigiusz Wilk

liczby = [91111, -7108079251, 405883740, 7942725602, 345220, 2915371507, 30, 9438104, 5736286, 984, 0]


def ile_cyfr(liczby):
    lista = [str(liczba) for liczba in liczby if liczba >= 0]
    # print(lista)
    liczby_str = [f'{x} ({len(x)} cyfr)' for x in lista]
    # liczby_str = [x + ' ({} cyfr)'.format(len(x)) for x in lista]

    return liczby_str


if __name__ == '__main__':
    print(ile_cyfr(liczby))
