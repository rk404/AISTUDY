def oblicz_potegi(liczba, wykładnik):
    potega = pow(liczba, wykładnik)
    return potega


liczba = int(input('Podaj liczbę: '))
wykładnik = int(input('Podaj wykładnik: '))
potega = oblicz_potegi(liczba, wykładnik)
print('Liczba podniesiona do potęgi: ', potega)


print(type(potega))