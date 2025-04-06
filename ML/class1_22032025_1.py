import numpy as np
import pandas as pd
import matplotlib.pyplot as plot

df = pd.read_csv('https://raw.githubusercontent.com/mateuszr/ml-course-1/main/datasets/advertising.csv')

print("Size of the data:", df.shape)


df.head() # wyświetlenie pierwszych 5 wierszy