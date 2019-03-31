class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Punkt({self.x}, {self.y})'

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Punkt(new_x, new_y)

    def __iadd__(self, other):
        print('Zawołano metodę __iadd__()')

        # nie ma zduplikowanego kodu
        return self.__add__(other)


if __name__ == '__main__':
    p1 = Punkt(2, 3)

    print(p1)

    p1 += Punkt(100, 100)

    print(p1)
