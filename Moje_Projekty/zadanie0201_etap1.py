class ParzysteLiczby:
    def __init__(self, end, start=0):
        self.liczba = start
        self.end = end

    def __next__(self):
        if self.liczba >= self.end:
            raise StopIteration
        zwracana = self.liczba
        self.liczba += 2
        return zwracana

    def __iter__(self):
        return self


if __name__ == '__main__':
    p_licz = ParzysteLiczby(100,4)
    print(list(p_licz))

