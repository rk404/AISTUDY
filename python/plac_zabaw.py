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
