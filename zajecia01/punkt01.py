class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Punkt({self.x}, {self.y})'

    # definiuje działanie operatora "+"
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Punkt(new_x, new_y)

    #definiuje działanie operatora "-"
    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Punkt(new_x, new_y)


if __name__ == '__main__':
    p1 = Punkt(2, 3)
    p2 = Punkt(7, 13)

    print(p1 + p2)
    print(p2 - p1)
    print(type(p1 + p2))


    # operator "+=" działa na podstawie naszego "+"
    p1 += Punkt(100, 100)
    print(p1)
