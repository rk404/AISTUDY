def krotka_na_slownik():
    krotka = (1, 2, 3, 4, 5)
    slownik = {i: i+1 for i in krotka}
    print(krotka)
    print(slownik)


krotka_na_slownik()