import numpy as np

np.random.seed(0)
a = np.random.randint(1, 10, 5)
print(a)
print("Wylosowane liczby to: ", a)

import pandas as pd
df = pd.DataFrame(a, columns=["Liczby"])
print(df)
print("Wylosowane liczby to: ", df)