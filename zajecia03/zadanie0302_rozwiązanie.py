# etap 1

liczby = [74.59, 52.812, 41.329, 23.323, 78.828, 74.6, 49.828, 3.685, 88.161, 62.02]

zaokraglone = [round(x, 1) for x in liczby]
print(zaokraglone)


# etap 2
from panstwa import panstwa

panstwa_na_m = [nazwa for nazwa in panstwa if nazwa[0] == 'M']
print(panstwa_na_m)

# etap 3

liczby = [74.59, 52.812, 41.329, 23.323, 78.828, 74.6, 49.828, 3.685, 88.161, 62.02]

polskie = [str(x).replace('.',',') for x in liczby]
print(polskie)

# etap 4

import random

losowe = [random.randint(0, 100000) / 1000 for x in range(10)]
print(losowe)
