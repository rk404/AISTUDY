slownik = {1: 'jeden', 'dwa': 2, 3.5: False}

for i in slownik.keys(): 
    print(i)

slownik = {1: 'jeden', 'dwa': 2, 3.5: False}
for i in slownik.values():
    print(i)


slownik2 = {1: 'jeden', 2: 'dwa', 3: 'trzy', 4: 'cztery'}
nowy_slownik = {klucz: wartosc for (klucz, wartosc) in slownik2.items() if klucz <=3}
print(nowy_slownik)


