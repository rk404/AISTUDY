import math as m
import cmath as cm
import numpy as np
import random as r

"""
liczba = float(input('Podaj liczbę: '))
pierwiastek = m.sqrt(liczba)
print('Pierwiastek z liczby', liczba, 'to:', pierwiastek)

licz2 = m.isqrt(8)  # 2   
print(licz2)   


kostka1 = r.randint(1, 6)
kostka2 = r.randint(1, 6)   
print('Wyrzucono', kostka1, 'oraz', kostka2)    
print('Suma oczek to:', kostka1 + kostka2) 


x = 3
y = 3
if x < y:
    print('x jest mniejsze od y')
elif x == y:
    print('x = y')
else:
    print('rsrr') 


rok = int(input('Podaj rok: '))
if (np.mod(rok,4) == 0 and np.mod(rok,100) != 0) or np.mod(rok,400) != 0:
    print('Tak')
else:
    print('Nie') """

num = int(input('Podaj liczbę: '))
suma = num
while num != 0:
    print("Suma:", suma)
    num = int(input('Podaj liczbę: '))
    suma += num
print('Koniec')


X = 0
while X < 10:
    print(X)
    #break
    X += 1

X = 0
Y = 1
while X < 10:   
    print(X)
    Y += 1  
    X += Y
  #  Y += 1



def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Przykład użycia
n = int(input("Podaj liczbę elementów ciągu Fibonacciego: "))
fib_sequence = fibonacci(n)
print(f"Ciąg Fibonacciego o długości {n}: {fib_sequence}") 


FIB1 = 0
FIB2 = 1
FIB_NEXT = 0
while FIB_NEXT < 100:   
    print(FIB1)
    FIB_NEXT = FIB1 + FIB2
    FIB1 = FIB2
    FIB2 = FIB_NEXT


for i in range(10):
    print(i)


num = int(input('Podaj liczbę: '))
suma = 0
for i in range(1, num+1):
    suma = suma + 1
print('Suma:', suma)


num = int(input('Podaj liczbę: '))
x = 0
fizz = 0
buzz = 0 
fizbuzz = 0
for i in range(1, num+1):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
        fizzbuzz += 1
    elif i % 5 == 0:
        print('Buzz')
        buzz += 1
    elif i % 3 == 0:
        print('Fizz')
        fiz += 1
    else:
        print(i)
print('Liczba wystąpień Fizz', x)