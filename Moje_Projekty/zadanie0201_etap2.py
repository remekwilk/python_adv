class ZakresLiczb:
    def __init__(self, end, start=0, krok=1):
        self.liczba = start
        self.end = end

        if krok <= 0:
            raise ValueError('Parament krok musi byc dodatni')
        self.krok = krok

    def __next__(self):
        if self.liczba >= self.end:
            raise StopIteration

        zwracana = self.liczba
        self.liczba += self.krok
        return zwracana

    def __iter__(self):
        return self


if __name__ == '__main__':
    p_licz = ZakresLiczb(10)
    print(list(p_licz))
    p_licz = ZakresLiczb(100,2,3)
    print(list(p_licz))

