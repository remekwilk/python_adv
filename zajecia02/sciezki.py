# dokumentacja tutaj: https://docs.python.org/3/library/pathlib.html

import pathlib

kat = pathlib.Path()

print(kat)
print(kat.absolute())

nowy_kat = kat / 'nowy_katalog'  # przeciążony operator "/"

print(nowy_kat)
print(nowy_kat.absolute())

print(f'Czy "{nowy_kat}" istnieje? {nowy_kat.exists()}')

# poniższa linijka stworzy katalog
nowy_kat.mkdir()

print(f'Czy "{nowy_kat}" istnieje? {nowy_kat.exists()}')
