import numpy as np

"""
tablica = np.array([[1,2, 3], [4, 5, 6], [7, 8, 9]])
print(tablica)
print(tablica.shape)
tablica.resize((3, 4))
print(tablica.shape)
print(tablica)

tablica[2, 2] = 9
tablica[2, 3] = 10
print(tablica)

np.append(tablica,[[11, 12, 13, 14]])
print(tablica) """

"""
tablica2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#tablica2_ilosc = np.linspace(1, 10, num=5)
tablica2_wyplaszczenie = tablica2.reshape(-1)
print(tablica2_wyplaszczenie)
#print(tablica2_ilosc)

tablica2_zmiana_wymiaru = tablica2.reshape(1, -1)
print(tablica2_zmiana_wymiaru)

tablica2_wyplaszczenie2 = tablica2.flatten()
print(tablica2_wyplaszczenie2) 

zera = np.zeros((3, 4))
print(zera) 
zera2d = np.zeros((1, 4, 2))
print(zera2d) """


#tablica_random = np.random.rand(30)



#for wartosc in np.nditer(tablica5):
#    print(wartosc, end=' ')


#print(tablica5)

#print(tablica5[1, :, 1])

#szukaj_przyste = np.where(tablica5 % 2 == 0)
#print(szukaj_przyste)


#np.savetxt('tablica5.csv', tablica5, delimiter=',')

#tablica6 = np.arange(1, 28).reshape(2,3,3)

#np.savetxt('tablica6.csv', tablica6, delimiter=',')


#tablica5 = np.arange(1, 31).reshape(3, 10)
"""for wartosc in np.nditer(tablica5% 2 != 0):
    wartosc = -1
    tablica5[wartosc] = -1
print(tablica5)"""

#tablica_nieparzyste = np.where(tablica5 % 2 != 0, -1, tablica5)
#print(tablica_nieparzyste)

tab1 = np.array([1,1,2,3,4,5,6,7,8,9])
tab2 = np.array([1,1,13,557,92,0,6,80,43,9])

tab3_find = np.where(tab1 == tab2)
print(tab3_find)



import pandas as pd

lista   = [1, 'test', 3, 4, 5, 6, 7, 8, 9, 10]

#seria = pd.Series(lista)
seria2 = pd.Series(lista, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
print(seria2['b'])

ramka = pd.DataFrame({'kolumna1': [1, 2, 3], 'kolumna2': [4, 5, 6]})
print(ramka)
