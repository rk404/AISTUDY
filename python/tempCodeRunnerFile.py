import pandas as pd

lista   = [1, 'test', 3, 4, 5, 6, 7, 8, 9, 10]

#seria = pd.Series(lista)
seria2 = pd.Series(lista, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
print(seria2['b'])

ramka = pd.DataFrame({'kolumna1': [1, 2, 3], 'kolumna2': [4, 5, 6]})
print(ramka)