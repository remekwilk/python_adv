tekst_z_liczbami = '2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67'

liczby_ale_str = tekst_z_liczbami.split()
print(liczby_ale_str)

liczby = [int(liczba) for liczba in liczby_ale_str]

print(liczby)
print(type(liczby[0]))


