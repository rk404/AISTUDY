import random


def impreza():
    liczba_gosci = int(input("Podaj liczbę gości: "))
    goscie = {}
    for i in range(liczba_gosci): 
        losowy_kolor = random.choice(["czerwony", "zielony", "niebieski", "żółty"])
        goscie[i+1] = losowy_kolor
    print(goscie)


impreza()