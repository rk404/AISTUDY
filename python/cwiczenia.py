def imie():
    print("Jak masz na imię?")
    imie = input("Imię: ")
    print("Witaj " + imie + "!")

imie()

"""
2. Napisz program, który rozwiąże w jakim wieku są osoby 
Maciek ma 21 lat 
Ula jest 6 lat starsza niż Maciek 
Czarek jest 20 lat starszy niż Ula 
Antek ma tyle lat co Czarek i Maciek razem 
Kasia ma tyle samo lat co Czarek 
 
Program powinien wydrukować wiek każdej osoby w oddzielnej linii 
"""

def wiek():
    maciek = 21
    ula = maciek + 6
    czarek = ula + 20
    antek = maciek + czarek
    kasia = czarek

    print("Maciek ma: ", maciek, "lat")
    print("Ula ma: ", ula, "lat")
    print("Czarek ma: ", czarek, "lat")
    print("Antek ma: ", antek, "lat")
    print("Kasia ma: ", kasia, "lat")
wiek()

"""
3. Napisz program, który zapyta użytkownika jakie jest jego ulubione zwierzę, a następnie 
odpowie, że to też jego ulubione zwierzę 
 
Przykładowy output: 
Jakie jest Twoje ulubione zwierzę? krowa 
Moje ulubione zwierzę to także krowa 
"""
def ulubione_zwierze():
    zwierze = input("Jakie jest Twoje ulubione zwierzę? ")
    print("Moje ulubione zwierzę to także " + zwierze)
ulubione_zwierze()

"""
4. Napisz program, który zapyta użytkownika o cyfrę, a następnie wydrukuje drugą potęgę tej 
liczby 
 
Przykładowy output: 
Podaj liczbę: 3 
3 do kwadratu to 9 
"""
def potega():
    liczba = int(input("Podaj liczbę: "))
    potega = liczba * liczba
    print(liczba, "do kwadratu to", potega)
potega()
"""
5. Poproś użytkownika o wprowadzenie długości każdego z boków trójkąta, a następnie wydrukuj 
wartość obwodu 
 
Przykładowy output: 
Jaka jest długość pierwszego boku? 1 
Jaka jest długość pierwszego boku? 2 
Jaka jest długość pierwszego boku? 3 
Odwód trójkąta to 6! 
"""
def obwod_trojkata():
    bok1 = int(input("Jaka jest długość pierwszego boku? "))
    bok2 = int(input("Jaka jest długość drugiego boku? "))
    bok3 = int(input("Jaka jest długość trzeciego boku? "))
    obwod = bok1 + bok2 + bok3
    print("Obwód trójkąta to", obwod)
obwod_trojkata()

"""
6. Użytkownik powinien wprowadzić temperaturę w stopniach Celsjusza, a program powinien mu 
powiedzieć jaka to temperaturę w stopniach Farenheita. 
Wzór na konwersję:  
F=C*9/5+32 
 
Przykładowy output: 
Podaj temperaturę [st. C]: 20 
20 stopni Celsjusza to 68 stopni Farenheita
"""
def celsjusz_na_farenheit():
    celsjusz = int(input("Podaj temperaturę [st. C]: "))
    farenheit = celsjusz * 9 / 5 + 32
    print(celsjusz, "stopni Celsjusza to", farenheit, "stopni Farenheita")
celsjusz_na_farenheit()

"""
7. Zapytaj użytkownika o podanie 2 liczb, a następnie wyświetl wynik odejmowania drugiej liczby 
od pierwszej liczby 
"""

def odejmowanie():
    print("Program do odejmowania: ");
    liczba1 = int(input("Podaj pierwszą liczbę: "))
    liczba2 = int(input("Podaj drugą liczbę: "))
    wynik = liczba1 - liczba2
    print("Wynik odejmowania to: ", wynik)
odejmowanie()

"""
8. Mad Libs: Napisz program, który zastąpi wyróżnione słowa, używając stałe 
Był sobie czarodziej o imieniu (imię), który uwielbiał jeść (owoc). 
(imię) zawsze trzymał zapas (liczba) (owoc) w swojej lodówce! 
Pewnego dnia, (imię) zdał sobie sprawę, że nie mogą zatrzymać tych wszystkich (owoc) dla siebie, 
więc sprzedał je na targu po (koszt) za sztukę, 
a za zarobione pieniądze kupił owoce do podzielenia się z całą wioską! 
Legenda głosi, że (ilość_lat) lat później (imię) nadal je owoce. 
"""

def stale():
    IMIE = "Rafal"
    OWOC = "banan"
    LICZBA = 4
    print("Był sobie czarodziej o imieniu", IMIE, "który uwielbiał jeść" , OWOC, "." 
    ,IMIE, "zawsze trzymał zapas", LICZBA, OWOC, "w swojej lodówce!")
stale()

"""
9. Waga Ziemianina na Marsie wynosi 37,8% ich wagi na Ziemi. Napisz program, który prosi 
Ziemianina o podanie swojej wagi na Ziemi i wyświetla obliczoną wagę na Marsie. 
"""

def waga_ziemianina():
    waga_na_ziemi = int(input("Ziemianinie podaj swoją wagę na ziemi: "))
    waga_na_marsie = waga_na_ziemi * 37.8/100
    print("Twoja waga na marsie to:", waga_na_marsie)
waga_ziemianina()

"""
10.  Oblicz pierwiastek kwadratowy liczby podanej przez użytkownika używając biblioteki math 
 
Przykladowy output: 
Podaj liczbę: 3 
Pierwiastek kwadratowy liczby 3.0 to 1.7320508075688772 

"""
import math
def pierwiastek_kw():
    liczba = int(input("Podaj liczbę: "))
    pierwiastek = math.sqrt(liczba)
    print("Pierwiastek z podanej liczby to: ", pierwiastek)
pierwiastek_kw()

"""
11.  Napisz program, który symuluje rzut dwiema kostkami i drukuje wyniki każdego rzutu, jak 
również sumę. 
 
Przykładowy output: 
Każda z kości ma 6 ścianek 
Pierwsza kość: 3 
Druga kość: 5 
Suma kości: 8

"""
import random
def rzut_kostkami():
    pierwsza_kostka = random.randint(1,6)
    druga_kostka = random.randint(1,6)
    print("Pierwsza kość: ", pierwsza_kostka)
    print("Pierwsza kość: ", druga_kostka)
    print("Suma kośći to: ", pierwsza_kostka + druga_kostka)
rzut_kostkami()

"""
12.  Napisz program, który wygeneruje 2 losowe liczby z zakresu od 0 do 99 i je dodać. Użytkownik 
próbuje zgadnąć odpowiedź. Program mu mówi czy zgadł dobrze 
 
Oczekiwany output: 
Jaka jest suma 58+45?   Jaka jest suma 58+45? 
Twoja odpowiedź: 103   Twoja odpowiedź: 130 
Odpowiedź prawidłowa!   Źle! Poprawna odpowiedź to 103 

"""
import random
def zgadnij_liczbe():
    pierwsza_liczba = random.randint(1,99)
    druga_liczba = random.randint(1,99)
    suma = pierwsza_liczba + druga_liczba
    print("Jaka jest suma liczb: ", pierwsza_liczba, "i ", druga_liczba, "?")
    moja_odp = int(input("Moja odpowiedź to: "))
    if suma == moja_odp:
        print("Prawda")
    else:
        print("Błąd")
zgadnij_liczbe()


"""
13.  Napisz program, który zapyta użytkownika o wiek, a następnie powie mu czy może głosować w 3 
fikcyjnych krajach: Etgidi (15), Siqira (57), Gmis (25). 
 
Przykładowy output: 
Ile masz lat? 21 
Możesz głosować w Etgidi, gdzie wiek wyborczy to 15 
Nie możesz głosować w Siqiri, gdzie wiek wyborczy to 57 
Nie możesz głosować w Gmis, gdzie wiek wyborczy to 25

"""

def glosowanie():
    wiek = int(input("Podaj swój wiek: "))
    if wiek >= 15 and wiek < 25:
        print("Możesz głosować w Etgidi, gdzie wiek wyborczy to 15")
        print("Nie możesz głosować w Siqiri, gdzie wiek wyborczy to 57")
        print("Nie możesz głosować w Gmis, gdzie wiek wyborczy to 25")
    elif wiek >= 57:
        print("Możesz głosować w Etgidi, gdzie wiek wyborczy to 15")
        print("Możesz głosować w Siqiri, gdzie wiek wyborczy to 57")
        print("Możesz głosować w Gmis, gdzie wiek wyborczy to 25")
    elif wiek < 15:
        print("Nie możesz głosować w Etgidi, gdzie wiek wyborczy to 15")
        print("Nie możesz głosować w Siqiri, gdzie wiek wyborczy to 57")
        print("Nie możesz głosować w Gmis, gdzie wiek wyborczy to 25")
    elif wiek >= 25 and wiek < 57:
        print("Możesz głosować w Etgidi, gdzie wiek wyborczy to 15")
        print("Nie możesz głosować w Siqiri, gdzie wiek wyborczy to 57")
        print("Możesz głosować w Gmis, gdzie wiek wyborczy to 25")
glosowanie()


"""
14.  Napisz program, który zasymuluje rzut dociążoną monetą. Szansa na wylosowanie orła: 70%
"""

import random 
def rzut_lewa_moneta():
    ORZEL=0.7 
    if random.random()<ORZEL: 
        print("Orzeł") 
    else: 
        print("Reszka")
rzut_lewa_moneta()

"""
15.  Napisz program, który powie użytkownikowi czy podany przez niego rok jest przestępny czy nie. 
Aby rok uznać za przestępny muszą być spełnione warunki: 
• jest podzielny przez 4 i niepodzielny przez 100 lub 
• jest podzielny przez 400

"""
import math
def rok_przestepny():
    rok = int(input("Podaj rok: "))
    if (rok%4 == 0 and (rok%100 != 0 or rok%400 == 0)):
        print("Przestępny.")
    else: 
        print("Nieprzestępny.")
rok_przestepny()

"""
16.  Napisz program, który wypisze ciąg Fibbonacciego do określonego limitu (np.: 1000) 
"""


def fibo():
    i = 0
    l1 = 0
    l2 = 0
    l3 = 0
    while i < 100:
        l2 = l1+l2
        l3 = l2+l3
        print(l2)
        print(l3)
        l1 = l1 + 1
        i = i + 1 
fibo()

def fib(): 
    LIMIT = 10000 
    fib1 = 0 
    fib2 = 1 
    while fib1 <= LIMIT: 
        print(fib1) 
        fib_next = fib1 + fib2 
        fib1 = fib2 
        fib2 = fib_next
fib()

"""
17.  Napisz program, który pyta użytkownika o liczbę i je dodaje. Program kończy się kiedy 
użytkownik poda 0.

"""

def dodawanie_w_petli():
    liczba = int(input("Podaj liczbę: "))
    suma = 0
    while liczba != 0:
        suma = suma+liczba
        print("Suma to: ", suma)
        liczba = int(input("Podaj liczbę: "))
dodawanie_w_petli()    

"""
18.  Napisz program, który zasymuluje “magic 8-ball”. Użytkownik zadaje pytanie, na które 
odpowiedź jest tak lub nie. Magiczna kula pokazuje mu odpowiedź. 
Możliwe odpowiedzi kuli: 
1) Tak 
2) Nie ma mowy 
3) Tylko kula wie 
4) Bezwzględnie 
5) Zapytaj później 
 
Przykładowy output: 
Czy dostanę awans? 
Tylko kula wie

"""
import random
def magiczna_kula():
    ODP_1 = "Tak!" 
    ODP_2 = "Nie ma mowy." 
    ODP_3 = "Tylko kula wie." 
    ODP_4 = "Bezwględnie." 
    ODP_5 = "Zapytaj później" 
    pytanie = input("Zadaj pytanie: ")
    
    while pytanie !="":
        odpowiedz = random.randint(1,5)
        if odpowiedz == 1:
            print(ODP_1)
        if odpowiedz == 2:
            print(ODP_2)
        if odpowiedz == 3:
            print(ODP_3)
        if odpowiedz == 4:
            print(ODP_4)
        if odpowiedz == 5:
            print(ODP_5)
        pytanie = input("Zadaj pytanie: ")
magiczna_kula()

"""
19.  Poproś użytkownika o podanie liczby, następnie napisz program, który policzy od 1 do tej liczby 
oraz wypisze je. Jeśli liczba jest podzielna przez 3 zastąp ją tekstem “Fizz”, jeśli jest podzielna 
przez 5 – zastąp ją napisem “Buzz”, natomiast jeśli jest podzielna przez 3 i 5 zastąp ją tekstem 
“FizzBuzz”. Na koniec podlicz numer “Fizz”, “Buzz” i “FizzBuzz”  
 
Oczekiwany output: 
1 
2 
Fizz 
4 
Buzz

"""

def fizzBuzz():
    liczba = int(input("Podaj liczbę: "))
    fizzbuzz = 0
    fizz = 0
    buzz = 0
    for i in range(1,liczba+1,1):
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
            fizzbuzz = fizzbuzz + 1
        elif i%3 == 0:
            print("Fizz")
            fizz = fizz + 1
        elif i%5 == 0:
            print("Buzz")
            buzz = buzz + 1
        else:
            print(i)
    print("Fizz: ", fizz, ", Buzz: ", buzz, ", FizzBuzzy: ", fizzbuzz)
fizzBuzz()


"""
20.  Poproś użytkownika o podanie liczby i napisz program, który doda wszystkie liczby od 1 do 
podanej (np.: 5 to 1+2+3+4+5) 
 
Przykładowy output: 
Podaj liczbę: 5 
Suma to 15

"""

def suma_w_petli_for():
    liczba = int(input("Podaj liczbę: "))
    suma = 0
    for i in range(1,liczba+1,1):
        suma = suma + i
    print("Suma: ", suma)
suma_w_petli_for()

"""
21.  Napisz pętlę while, która zaczyna się od ostatniego znaku w napisie i działa od końca, do 
pierwszego znaku, wypisując każdą literę w osobnej linii, w odwrotnej kolejności. 

"""

def iter_w_ciagu():
    ciag = input("Podaj słowo: ")
    indeks = len(ciag)-1
    while indeks >= 0:
        litera = ciag[indeks]
        print(litera)
        indeks = indeks - 1
iter_w_ciagu()

"""
22.  Napisz program, który policzy ile z każdej litery występuje w słowie “rabarbar”

"""

def liczenie_liter():
    CIAG = "rabarbar"
    i = 0
    r = 0
    a = 0
    b = 0
    while i <= len(CIAG)-1:
        if CIAG[i] == "r":
            r = r + 1
        elif CIAG[i] == "a":
            a = a + 1
        elif CIAG[i] == "b":
            b = b + 1
        i = i + 1
    print("Litery r: ", r, "a: ", a, "b: ",b)
liczenie_liter()


"""
23.  Napisz program, który poprosi użytkownika o 5 słów i powie mu które z nich jest najdłuższe oraz 
ile ma liter 

"""

def dlugosc_slow():
    dl = 0
    for i in range(5):
        slowo = input("Podaj slowo: ")
        new_dl = len(slowo)
        if new_dl > dl:
            longest_word = slowo
            dl = len(longest_word)
    print("Słowo: ", longest_word, "Dlugosc: ", dl)
dlugosc_slow()
"""
24.  Napisz program, który podniesie każdy z elementów listy do kwadratu     
"""
def kwadraty():
    lista = [2,4,5]
    for i in range(len(lista)):
        lista[i] = int(lista[i])*int(lista[i])
    print(lista)
kwadraty()

"""
25.  Napisz program, który policzy ile jest elementów w liście (bez użycia funkcji len())
"""

def liczba_elementow():
    lista = [2,4,5]
    licznik = 0
    for element in lista:
        licznik = licznik + 1
    print(licznik)
liczba_elementow()

"""
26.  Napisz program, który doda pola 3 trójkątów 
 
Trójkąt 1:  Trójkąt 2:  Trójkąt 3: 
a=3   a=8   a=7 
h=5   h=12   h=4 
 
Oczekiwany output: 
Pole wszystkich trójkątów to: 69.5

"""

def pole_trojkata(a,h):
    pole = 0.5*a*h
    return pole

def pola_trojkatow():
    tr1 = pole_trojkata(3,5)
    tr2 = pole_trojkata(8,12)
    tr3 = pole_trojkata(7,4)
    suma = tr1+tr2+tr3
    print(suma)
pola_trojkatow()

"""
27.  Napisz program, który przyjmuje integer i drukuje jego cyfrę jedności 
 
748 
 
 
cyfra setek   cyfra dziesiątek   cyfra jedności 
 
Przykładowy output: 
Podaj liczbę: 748 
Cyfra jedności to 8

"""

def cyfra_jednosci():
    liczba = int(input("Podaj liczbę: "))
    liczba_j = liczba%10
    print(liczba_j)
cyfra_jednosci()


"""
28.  Zamień krotki: 
 
krotka1 = (0, 45, 67) 
krotka2 = (99, 65, 32) 
 
Oczekiwany output: 
krotka1: (99, 65, 32)  
krotka2: (0, 45, 67) 

"""

def zamiana_krotek():
    krotka1 = (0, 45, 67) 
    krotka2 = (99, 65, 32) 
    krotka3 = (0, 45, 67)
    krotka1 = krotka2
    krotka2 = krotka3
    print(krotka1)
    print(krotka2)
zamiana_krotek()

"""
29.  Skopiuj kawałek jednej krotki do innej 
krotka1 = (54, 7, 24, 67, 22, 97, 56) 
 
Oczekiwany output: 
krotka2 = (67, 22, 97) 

"""

def wycinanie_krotki():
    krotka1 = (54, 7, 24, 67, 22, 97, 56)
    krotka2 = krotka1[3:6]
    print(krotka2)
wycinanie_krotki()

"""
30.  Utwórz słownik, a następnie podnieś jego wszystkie wartości do kwadratu jeśli wartość jest 
liczbą całkowitą 
 
slownik = {1:1, 2:2.5, 3:3.9, 4:4, 5:4.3,6:4.5} 

"""

def kwadrat_slownika():
    slownik = {1:1, 2:2.5, 3:3.9, 4:4, 5:4.3,6:4.5} 
    for i in slownik:
        if slownik[i] == int(slownik[i]):
            slownik[i] = slownik[i]**2
    nowy_slownik = {klucze:wartosc**2 for (klucze,wartosc) in slownik.items() if wartosc==int(wartosc)} 
    print(slownik)
    print(nowy_slownik)


kwadrat_slownika()

"""
31. Utwórz krotkę i przerób ją na klucze słownika. Wartości mogą być dowolne.
"""


def krotka_na_slownik():
    krotka = (1, 2, 3, 4, 5)
    slownik = {i: i+1 for i in krotka}
    print(krotka)
    print(slownik)


krotka_na_slownik()


"""
32. Pamiętacie zadanie z rabarbarem?
Teraz w końcu możecie wybrać dowolne słowo :D
Napisz program, który policzy ile z każdej litery występuje w słowie “rabarbar”
Oczekiwany output:
W slowie "rabarbar" występuja 3 litery "r“
W slowie "rabarbar" występuja 3 litery "a“
W slowie "rabarbar" występuja 2 litery "b"
"""


def liczenie_liter_slow():
    slownik = {}
    slowo = input("Podaj słowo: ")
    for element in slowo:
        if element not in slownik:
            slownik[element] = 1
        else:
            slownik[element] += 1
    print(slownik)
    for i in slownik:
        print("W słowie", slowo, "występują", slownik[i], "litery", i)


liczenie_liter_slow()


"""
33. Napisz program, który poda do funkcji listę I wydrukuje kolejno jej elementy
Lista: ['t', [9, 0], 5.7, 6437]
"""


def drukuj_liste(lista):
    for i in lista:
        print(i)


def dane_do_druku():
    Lista = ['t', [9, 0], 5.7, 6437]
    drukuj_liste(Lista)


dane_do_druku()

"""
34. Napisz program, który wypisze liczbę elementów, które są unikalne na liście.
lista = ['k', 2, 5, 2, 'mop', 5.4, 'k', 8, False]
Oczekiwany output:
Liczba unikalnych elementów to 7

"""


def unikale_elementy_listy():
    lista = ['k', 2, 5, 2, 'mop', 5.4, 'k', 8, False]
    bufor = []
    licznik = 0
    for i in lista:
        if i not in bufor:
            licznik = licznik + 1
            bufor.append(i)
    print(licznik)


unikale_elementy_listy()


"""
35. Napisz program, który przyjmie liczbę i wypisze wszystkie możliwe dzielniki tej liczby.
Przykładowy output:
Podaj liczbę: 8
1
2
4
8
"""


def dzieliniki():
    liczba = int(input("Podaj liczbę: "))
    for i in range(liczba):
        obecna_liczba = i+1
        if liczba % obecna_liczba == 0:
            print(obecna_liczba)


dzieliniki()


"""
36. Poproś użytkownika, żeby podał string oraz integer. Program powinien wydrukować podany
string podaną ilość razy.
Przykładowy output:
Podaj string: Cześć!
Podaj liczbę: 3
Cześć!
Cześć!
Cześć!
"""


def drukuj_string():
    tekst = input("Podaj tekst: ")
    ile_razy = int(input("Podaj ile razy ma się wydrukować: "))
    for i in range(ile_razy):
        print(tekst)


drukuj_string()

"""
37. Zapytaj użytkownika o słowo, następnie jaka to część mowy (rzeczownik, czasownik,
przymiotnik)
Jeśli część mowy to 0, zakładamy że słowo to rzeczownik, zdanie brzmi “Super! Od dawna chciałam
dodać _____ do mojej kolekcji”
Jeśli część mowy to 1, zakładamy że słowo to czasownik, zdanie brzmi: “Jest taka piękna pogoda, że
aż się chce _____”
Jeśli część mowy to 2, zakładamy że słowo to przymiotnik, zdanie brzmi: “Patrząc za okno, niebo jest
wielkie I ______”
Weź pod uwagę przypadek, kiedy słowo podane przez użytkownika nie jest ani rzeczownikiem, ani
czasownikiem, ani przymiotnikiem
Przykładowy output:
Podaj słowo: kamień
Jaka to część mowy? (0 – rzeczownik, 1 – czasownik, 2 – przymiotnik): 0
Super! Od dawna chciałam dodać kamień do mojej kolekcji
"""


def jaka_to_czesc_mowy():
    slowo = input("Podaj słowo: ")
    czesc_mowy = int(input("Jaka to część mowy? (0 - rzeczownik, 1 - czasownik, 2 - przymiotnik): "))
    if czesc_mowy == 0:
        print("Super! Od dawna chciałam dodać", slowo,  "do mojej kolekcji")
    elif czesc_mowy == 1:
        print("Jest taka piękna pogoda, że aż się chce ", slowo)
    elif czesc_mowy == 2:
        print("Patrząc za okno, niebo jest wielkie I ", slowo)
    else:
        print("Błędne dane")


jaka_to_czesc_mowy()

"""
38. Napisz program, który przyjmie liczbę i zwróci jej dwukrotność
Przykładowy output:
Podaj liczbę: 8
Dwukrotność 8 to 16
"""


def dwukrotnosc(liczba):
    wynik = liczba+liczba
    return wynik


liczba = int(input("Podaj liczbę: "))
wynik = dwukrotnosc(liczba)
print("Dwukrotność",  liczba, "to", wynik)


"""
39. Napisz program, który powie Ci czy liczba, którą podał użytkownik jest parzysta czy nieparzysta
Przykładowy output:
Podaj liczbę: 43
43 o liczba nieparzysta
"""


def parzystosc(liczba):
    if liczba % 2 == 0:
        wynik = "Parzysta"
    else:
        wynik = "Nieparzysta"
    return wynik


liczba = int(input("Podaj liczbę: "))
wynik = parzystosc(liczba)
print("Podana liczba jest: ", wynik)


"""
40. Będziemy liczyć do 10, chyba że po drodze nam się odechce
Napisz funkcję, która wydrukuje liczby od 1 do 10 oraz fukncję, która zadecyduje czy chce jej się to
liczyć.
Prawdopodobieństwo wydruku każdej z kolejnych liczb to 30%.
Na końcu zawsze musi wyskoczyć napis: “No to tyle”
Przykladowy output:
Będę liczyć do 10, chyba że mi się odechce.
1
2
No to tyle

"""


import random


def liczenie_do_czasu():
    zakres = 10
    for i in range(zakres):
        prawdopodobienstwo_wydruku = random.random()
        if prawdopodobienstwo_wydruku < 0.3:
            print(i+1)
        else:
            print("Not to tyle")
            break


liczenie_do_czasu()


"""
41. Stwórz pusty plik, następnie poproś użytkownika, żeby podał treść.
Sprawdź czy możesz zapisać tę treść do pliku.
Jeśli tak, to zapisz.
Na koniec powiedz użytkownikowi ile podał znaków.
"""


def zapis_dp_pliku():
    plik = open("plik_01.txt", "a")
    tresc = input("Podaj treść: ")
    if plik.writable():
        plik.write(tresc)
        plik.write("\n")
        liczba_znakow = len(tresc)
        print("Podałeś ", liczba_znakow, "znaków.")
    else:
        print("Brak uprawnień do zapisu")
    plik.close()


zapis_dp_pliku()


"""
42. Napisz program, który przeczyta zawartość pliku linijka po linijce in wydrukuje treść w taki sam
sposób.
"""


def odczyt_linia_po_lini():
    plik = open("plik_01.txt", "r")
    dane = plik.readlines()
    for i in dane:
        if i.isspace():
            print(i)


odczyt_linia_po_lini()


"""
43. Stwórz tablicę, a następnie zamień wszystkie liczby nieparzyste na wartość -1
"""

import numpy as np
def tablica_nieparzysta():
    tab1 = np.arange(10).reshape(2, 5)
    tab1[tab1%2==1] = -1
    print(tab1)
tablica_nieparzysta()


"""
44. Stwórz tablicę, która będzie posiadała tylko element wspólne poniższych tablic
tab1 = [0 1 2 3 4 5 6 7 8 9]
tab2 = [3 1 13 557 92 0 6 80 43 9]
"""


import numpy as np
def tablica_wsp():
    tab1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    tab2 = np.array([3, 1, 13, 557, 92, 0, 6, 80, 43, 9])
    tab3 = np.where(tab1 == tab2)
    print(tab3)
tablica_wsp()

"""
44. Stwórz tablicę, która będzie posiadała tylko element wspólne w tych samych miejscach poniższych tablic
tab1 = [0 1 2 3 4 5 6 7 8 9]
tab2 = [3 1 13 557 92 0 6 80 43 9]
"""
import numpy as np
def tablica_wsp():
    tab1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    tab2 = np.array([3, 1, 13, 557, 92, 0, 6, 80, 43, 9])
    tab3 = np.where(tab1 == tab2)[0]
    print("Wspólne elementy:", tab3)
tablica_wsp()