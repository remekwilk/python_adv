class ZakresLiczb:
    def __init__(self, end, start=0, step=1):
        self.liczba = start
        self.end = end

        if step <= 0:
            raise ValueError('Parametr "step" musi być dodatni')
        self.step = step


    def __next__(self):
        if self.liczba >= self.end:
            raise StopIteration

        zwracana = self.liczba
        self.liczba += self.step
        return zwracana

    def __iter__(self):
        return self


if __name__ == '__main__':
    pl = ZakresLiczb(10)
    print(list(pl))

    pl = ZakresLiczb(20, 10)
    print(list(pl))

    pl = ZakresLiczb(30, 10, 3)
    print(list(pl))

