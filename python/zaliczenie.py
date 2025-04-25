# 1.

def poprawny_mail():
    mail = input("Podaj adres mailowy: ")
    if "@" not in mail: 
        print("Brak znaku @ !")
    elif "." not in mail:
        print("Brak . w adresie mailowym !")
    else:
        print("Adres mailowy jest poprawny")


poprawny_mail()



# 2.


import numpy as np


def zmiana_w_tablicy():
    tab = np.arange(64).reshape(8, 8)
    tab[-1, :] = 0 # wiersz
    tab[:, -1] = 0 # kolumna
    print(tab)


zmiana_w_tablicy()

# 3.


import random


def impreza():
    liczba_gosci = int(input("Podaj liczbę gości: "))
    goscie = {}
    for i in range(liczba_gosci): 
        losowy_kolor = random.choice(["czerwony", "zielony", "niebieski", "żółty"])
        goscie[i+1] = losowy_kolor
    print(goscie)


impreza()
