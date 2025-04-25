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



plik = open("C:\\Users\\rafalkaminski\\AISTUDY\\AISTUDY\\python\\pliki\\Friendly Competition2.csv", "r")
dane = plik.readlines()
plik.close()

"""
otwórz plik friendly competition.csv i zapisz dane do zmiennej korzystając z pandas
"""
import pandas as pd
df = pd.read_csv("Friendly Competition.csv")
print(df)

#pozostaw tylko dane z wartościami
df = df.dropna(axis=0)
print(df)

pętla malejąca

for i in range(10, 0, -1):
    print(i)

    program czytający od końca teks podany przez użytkownika
zmienna = input("Podaj tekst: ")
for i in range(len(zmienna)-1, -1, -1):
    print(zmienna[i], end='')



def potega(x,y):
   z = x ** y
   return z
def main():
    x = int(input("Liczba: "))
    y = int(input("do potęgi: "))
    print(potega(x,y))
main()


def petla():
   zmienna = "Koty"
   slownik = {}
   i = 0
   k = 1
   while i < len(zmienna):
    print(i)
    slownik[k] = zmienna[i]
    k = k + 1
    i = i + 1
    print(slownik)
petla()
      


def rabarbar():
    slowo = input("Podaj słowo: ")
    slownik = {}
    i = 0
    for i in range(len(slowo)):
      if slowo[i] not in slownik:
         slownik[slowo[i]] = 1
    #    slownik.update({slowo[i]:1})
      else:
         slownik[slowo[i]] = slownik[slowo[i]] + 1
    #     slownik.update({slowo[i]:slownik.get(slowo[i])+1})
    print(slownik)
rabarbar()


def pole_trojkata(a,h):
    pole = 0.5*a*h
    return pole

def wywolanie():
    input()


Stwórz tablice 8 x 8 i wypełnij ją liczbami od 1 do 64. Zamień ostatni wiersz i ostatnią kolumnę na 0.

import numpy as np
tablica = np.arange(1, 65).reshape(8, 8) 
print(tablica)



    




    




