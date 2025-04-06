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


tablica5 = np.arange(1, 28).reshape(3,3, 3)
#for wartosc in np.nditer(tablica5):
#    print(wartosc, end=' ')


#print(tablica5)

#print(tablica5[1, :, 1])

szukaj_przyste = np.where(tablica5 % 2 == 0)
print(szukaj_przyste)