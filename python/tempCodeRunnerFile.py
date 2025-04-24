def kwadrat_slownika():
    slownik = {1:1, 2:2.5, 3:3.9, 4:4, 5:4.3,6:4.5} 
    for i in slownik:
        if slownik[i] == int(slownik[i]):
            slownik[i] = slownik[i]**2
    nowy_slownik = {klucze:wartosc**2 for (klucze,wartosc) in slownik.items() if wartosc==int(wartosc)} 
    print(slownik)
    print(nowy_slownik)
kwadrat_slownika()