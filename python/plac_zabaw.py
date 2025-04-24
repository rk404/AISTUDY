num1 = int(input("Podaj pierwsza liczbe: "))
num2 = int(input("Podaj druga liczbe: "))

num3 = num1 + num2
print("Suma liczb to: ", num3)

print(f"Pierwsza liczba to: {num1}, druga liczba to: {num2}, a ich suma to: {num3}")
print("Pierwsza liczba to: {}, druga liczba to: {}, a ich suma to: {}".format(num1, num2, num3))


print("he\’s a boy\n") 

import numpy as np

np.random.seed(0)
a = np.random.randint(1, 10, 5)
print(a)
print("Wylosowane liczby to: ", a)

import pandas as pd
df = pd.DataFrame(a, columns=["Liczby"])
print(df)
print("Wylosowane liczby to: ", df)

slownik = {1: 'jeden', 2: 'dwa', 3: 'trzy'}
slownik[4] = 'Pięć'
print(slownik)


plik = open("test_plik.txt")
odczyt =plik.read()
plik.close()


tablica2d = ([[3, 5, 2], [5, 2, 7]])
# dostęp do elementów tablicy
for element in tablica2d:
 print(element)

tablica2d = ([[3, 5, 2], [5, 2, 7]])
#dostęp do poszczególnych wartości tablicy
for element in tablica2d:
    for wartosc in element:
        print(wartosc)

import numpy as np
tablica = np.arange(1, 20, 2).reshape(2, 5)
print(tablica)

maska = tablica > 10
zamaskowane = np.ma.masked_where(maska, tablica)
print(zamaskowane)

np.savetxt("plik_testowy.csv", tablica, delimiter=",")



plik = open("\\python\\Friendly Competition.csv", "r")
dane = plik.readlines()
plik.close()

"""
otwórz plik friendly competition.csv i zapisz dane do zmiennej korzystając z pandas
"""
import pandas as pd
df = pd.read_csv("Friendly Competition.csv")
print(df)

"""


