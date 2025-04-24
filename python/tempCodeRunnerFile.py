import numpy as np  
def mediana_tablicy():
    tab1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    mediana = np.median(tab1)
    print("Mediana elementów tablicy to: ", mediana)
mediana_tablicy()