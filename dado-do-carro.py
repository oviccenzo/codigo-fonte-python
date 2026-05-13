import pandas as pd
import numpy as np

df = pd.read_excel("dado-do-carro-1.xlsx")

df

#todas as funções matematica

print(df.mean(numeric_only=True))

print(df.median(numeric_only=True))

print(df.mode())

print(df.count())

print(df.idxmax())

print(df.idxmin())

print(df.sum())

print(df.corr(numeric_only=True))

print(df.describe())

print(df.value_counts())

print(df.min())

print(df.max())

print(df.std(numeric_only=True))

print(df.nunique())

print(df.var(numeric_only=True))

print(df.round())

print(df.select_dtypes(include=np.number).abs())
