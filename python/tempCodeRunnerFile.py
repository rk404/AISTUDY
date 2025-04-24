import pandas as pd
df = pd.read_csv("Friendly Competition.csv")
print(df)

#pozostaw tylko dane z wartościami
df = df.dropna(axis=0)
print(df)