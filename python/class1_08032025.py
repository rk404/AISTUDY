print('Ten program dodaje 2 liczby')
num1 = input('Wpisz pierwszą liczbę: ')
num1 = int(num1)
num2 = input('Wpisz drugą liczbę: ')
num2 = int(num2)
print('Wynik dodawania', num1, 'i', num2, 'to:', num1+num2)

if num1+num2 == 42:
    print('To jest odpowiedź na pytanie o życie, wszechświat i całą resztę!')
else:
    print('To nie jest odpowiedź na pytanie o życie, wszechświat i całą '
          'resztę!')

num3 = input('Wpisz trzecią liczbę: ')
num3 = float(num3)
num4 = input('Wpisz czwartą liczbę: ')
num4 = float(num4)
print('Wynik dzielenia', num3, 'przez', num4, 'to:', num3/num4)
print(f"{num3} i liczba {num4}")

num5 = float(input('Wpisz czwartą liczbę: '))

imie = input('Jak masz na imie?');
print('Witaj', imie)

maciek = 21
print('Maciek ma lat: ', maciek)
ula = 21+6
print('Ula ma lat: ', ula)
czarek = ula+20
print('Czarek ma lat: ', czarek)
antek = czarek +maciek
print('Antek ma lat: ', antek)
kasia = czarek
print('Kasia ma lat: ', kasia)

zwierz = input('Jakie jest Twoje ulubione zwierze?')
print('Twoje ulubione zwierze to:', zwierz)

bok1 = input('Podaj długość boku 1: ')
bok2 = input('Podaj długość boku 2: ')
bok3 = input('Podaj długość boku 3: ')
obwod = float(bok1) + float(bok2) + float(bok3)
print('Obwód trójkąta o bokach', bok1, bok2, bok3, 'to:', obwod)

liczba = input('Podaj liczbę: ')
potega = pow(float(liczba), 2)
print('Liczba podniesiona do potęgi:', potega)

temperatura = float(input('Podaj temperaturę w stopniach Celsjusza: '))
fahrenheit = temperatura * 1.8 + 32
print('Temperatura w stopniach Fahrenheit to:', fahrenheit)


print('he\'s a boy')

print('przykład \n nowej linii')
print('przykład \t tabulatora')
print('przykład\r tab')


liczba = int(input('Podaj liczbę: '))
potega = pow(liczba, 2)
potęga3 = liczba**3
print('Liczba podniesiona do potęgi:', potega)
print('Liczba podniesiona do potęgi 3:', potęga3)

liczba1 = int(input('Podaj pierwszą liczbę: '))
liczba2 = int(input('Podaj drugą liczbę:'))
roznica = liczba1 - liczba2
print('Różnica liczb', liczba1, 'i', liczba2, 'to:', roznica)

print('Witaj w programie, który oblicza pole trójkąta')
podstawa = float(input('Podaj długość podstawy trójkąta: '))

print('Podaj wysokość trójkąta')

lista = [1, 2, 3, 4, 5]

for i in lista:
    print(i)


with open('plik.txt', 'w') as f:
    f.write('Hello, World!')

with open('plik.txt', 'r') as f:
    print(f.read())


def dodaj(a, b):
    return a + b


def oblicz_potegi(liczba, wykładnik):
    potega = pow(liczba, wykładnik)
    return potega


liczba = int(input('Podaj liczbę: '))
wykładnik = int(input('Podaj wykładnik: '))
potega = oblicz_potegi(liczba, wykładnik)
print('Liczba podniesiona do potęgi: ', potega)


print(type(potega))
