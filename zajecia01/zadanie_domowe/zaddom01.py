class CzasBiegacza:

    def __init__(self, minuty, sekundy):
        self._minuty = self.setMinutes(minuty)
        self._sekundy = self.setSeconds(sekundy)

    def __repr__(self):
        return f'czas: {self._minuty}min, {self._sekundy}sek'

    def setMinutes(self, minuty):
        if minuty >= 0:
            return minuty
        else:
            raise ValueError

    def setSeconds(self, sekundy):
        if 0 <= sekundy <= 59:
            return sekundy
        else:
            raise ValueError

    def __lt__(self, other):
        if self._minuty < other._minuty:
            return True
        elif self._sekundy < other._sekundy:
            return True
        else:
            return False

    def __eq__(self, other):
        if self._minuty == other._minuty and self._sekundy == other._sekundy:
            return True
        else:
            return False

    def __add__(self, other):
        _minuty = self._minuty + other._minuty
        _sekundy = self._sekundy + other._sekundy

        if _sekundy > 59:
            _minuty += 1
            _sekundy -= 60
        return CzasBiegacza(_minuty, _sekundy)

    def __sub__(self, other):
        if self._minuty < other._minuty and self._sekundy < other._sekundy:
            raise ValueError
        else:
            _minuty = self._minuty - other._minuty
            _sekundy = self._sekundy - other._sekundy
            if _sekundy < 0:
                _minuty -= 1
                _sekundy += 60
        return CzasBiegacza(_minuty, _sekundy)


if __name__ == '__main__':
    # tutaj można pisać dowolny kod, nie wpływa to na testy
    cz1 = CzasBiegacza(3, 3)
    cz2 = CzasBiegacza(3, 2)

    print(cz1)
    print(cz2)
    print(cz1 + cz2)
    print(cz1 - cz2)
