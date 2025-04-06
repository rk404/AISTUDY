import math as m
import numpy as nu

def wydruk():
    print("Hello World!")   


def podwojny():
    wydruk()
    wydruk()


def ocena():
    procent = float(input('Podaj procent: '))
    if procent >= 50:
        print('Zdałeś')
    elif procent < 50:
        print('Nie zdałeś')


def dodawania(a, b):
    suma = a + b
    return suma


def pole_trojkata(a, h):
    pole = 0.5 * a * h
    return pole


def cyfra_jednosci(a):
    cyfra = a%10
    return cyfra


def ciag_znakow():
    zmienna = 'Ala ma kota'
    for i in range(len(zmienna)):
        print(zmienna[i])


def wypisz_litery():
    zmienna = 'Ala ma kota'
    ilosc_znakow = len(zmienna)
    while ilosc_znakow > 0:
        print(zmienna[ilosc_znakow-1])
        ilosc_znakow -= 1


def ilosc_wystapien():
    zmienna = 'rabarbar'
    ilosc_a = 0
    ilosc_r = 0
    ilosc_b = 0
    for i in range(len(zmienna)):
        if zmienna[i] == 'a':
            ilosc_a += 1
        elif zmienna[i] == 'r':
            ilosc_r += 1
        elif zmienna[i] == 'b':
            ilosc_b += 1
    print('Ilość wystąpień litery r:', ilosc_r)
    print('Ilość wystąpień litery a:', ilosc_a)
    print('Ilość wystąpień litery b:', ilosc_b)
    diff_letters = len(set(zmienna))
    #count_diff_letters = nu.unique(zmienna, return_counts=True)
    #print('Ilość różnych liter:', count_diff_letters)
    print('Ilość różnych liter:', diff_letters)




def main():
    """podwojny() 
    ocena()
    total = dodawania(2, 3)
    print(total)
    tr1 = pole_trojkata(3, 5)
    tr2 = pole_trojkata(8, 12)
    tr3 = pole_trojkata(7, 4)
    suma = tr1 + tr2 + tr3
    print('Suma pól trójkątów:', suma)
    liczba = int(input('Podaj liczbę: '))
    cyfra_jed = cyfra_jednosci(liczba)
    print('Liczba jednosci: ', cyfra_jed)
    wypisz_litery()"""
    ilosc_wystapien()

main()   

lista = [12, 44, 33]
nowa_lista = [x for x in lista]
print(nowa_lista)

lista = [12, 44, 33]
nowa_lista2 = [print(x**3) for x in lista if x > 70]


lista3 = [34.6, -34.7, -10.4, 23, 90.8, 11.3, 32.5]
nowa_lista3 = [print(int(x)) for x in lista3 if x > 0]

lista = []
for x in lista:
    print('lista')


slowo1 = input('Podaj pierwsze słowo: ')
slowo2 = input('Podaj drugie słowo: ')  
slowo3 = input('Podaj trzecie słowo: ')
slowo4 = input('Podaj czwarte słowo: ')
slowo5 = input('Podaj piąte słowo: ')
lista_slow = [slowo1, slowo2, slowo3, slowo4, slowo5]
print('Najdluzsze slowo:', max(lista_slow, key=len), 'o długości:', len(max(lista_slow, key=len)))

dlugosc = 0
for x in range(5):
    slowo = input('Podaj słowo: ')
    if len(slowo) > dlugosc:
        dlugosc = len(slowo)
        najdluzsze_slowo = slowo
print('Najdluzsze slowo:', najdluzsze_slowo, 'o długości:', dlugosc)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_kwadratow = [x**2 for x in lista]
print(lista_kwadratow)

lista_kwadratow2 = [pow(x,2) for x in lista]
print(lista_kwadratow2)


lista_r = [1, 'słowo', False, 3.14]
#print(dir(lista_r))
print(help(lista_r))


# append, lista.insert(1,'ziemniak'), index, remove

lista5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista5.remove(5)
print(lista5)


for i in lista5:
    if i > 5:
        lista5.remove(i)    
print(lista5)        

krotka = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(krotka[2])


warzywa = ('pomidor', 'ziemniak', 'marchewka', 'cebula', 'seler')
('czerwony','brązowy','pomoarańczowy','biały','biały') = warzywa


krotka2 = (43,[],()))



krotka3 = (0,45,67)
krotka4 = (99,65,32)    
krotka3, krotka4 = krotka4, krotka3
print(krotka3, krotka4)


krotka5 = (54,7,24,67,22,97,56)
krotka6 = krotka5[3:-1]
print(krotka6)
