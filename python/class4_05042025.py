plik = open("plik.txt", "w")
plik.write("To jest plik tekstowy\n")
print(plik.read())
plik.close()



plik2 = open("plik_test.txt","w")
zawartosc = input("Podaj coś: ")
print(plik2.mode)
if plik2.mode == "w":
    print("Plik otwarty w trybie odczytu")  
    plik2.write(zawartosc)
else:
    print("Plik nie jest otwarty w trybie odczytu")
plik2.close()

plik2 = open("plik_test.txt", "r")
zawartosc = plik2.read()
if 'r' in zawartosc:
    print("tak")
else:
    print("nie")
print(zawartosc)
plik2.close()

zawartosc_dodana = "ereere"
plik2 = open("plik_test.txt", "a+")
plik2.write(zawartosc_dodana)
zawartosc = plik2.read()
print(zawartosc)
plik2.close()


