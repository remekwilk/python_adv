class Wyraz:
    """
    Klasa definiująca wyrazy, które można porównywać po liczbie liter
    """

    def __init__(self, tekst):
        self._tekst = tekst

    def __repr__(self):
        return self._tekst

    def __lt__(self, other):
        if len(self._tekst) < len(other._tekst):
            return True
        else:
            return False

    def __le__(self, other):
        if len(self._tekst) <= len(other._tekst):
            return True
        else:
            return False

    def __eq__(self, other):
        if len(self._tekst) == len(other._tekst):
            return True
        else:
            return False


if __name__ == '__main__':
    m = Wyraz('Magik')
    p = Wyraz('Prestidigitator')

    print(f'{m} > {p} : {m > p}')
    print(f'{m} < {p} : {m < p}')

    print(f'{m} >= {p} : {m >= p}')
    print(f'{m} <= {p} : {m <= p}')

    print(f'{m} == {p} : {m == p}')
    print(f'{m} != {p} : {m != p}')
