print((2+2)/2)


INCH_TO_CM = 2.54

inch = float(input('Podaj długość w calach: '))
cm = inch * INCH_TO_CM  # przeliczenie cali na centymetry
print('Długość w centymetrach to:', cm)


IMIE = 'Jan'
OWOC = 'jabłko'
LICZBA = 5
KOSZT = 10.5
ILE_LAT = 20
print('Był sobie czarodziej o imieniu ', IMIE, 'który lubił jeść', 
      OWOC,' i miał', LICZBA, OWOC)
print('Koszt zakupu', LICZBA, OWOC, 'to:', LICZBA * KOSZT, 'zł')
print('Czarodziej miał', ILE_LAT, 'lat.')

PROCENT_WAGI = 37.8
waga_na_ziemi = float(input('Podaj swoją wagę w kilogramach: '))
waga_na_marsie = waga_na_ziemi * PROCENT_WAGI / 100
print('Twoja waga na Marsie wynosi:', waga_na_marsie, 'kg')


