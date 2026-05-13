#Importação da biblioteca e mostrando a tabela do dados dos carro

import pandas as pd
import numpy as np

df = pd.read_excel("dado-do-carro-1.xlsx")

df

df.head()

colunas = ['cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']
df = df[colunas]

df

#todas as funções matematica

print(df.mean(numeric_only=True))

df.head()

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

#median

print(df.median(numeric_only=True) + df.median(numeric_only=True))

print(df.median(numeric_only=True) + df.mode(numeric_only=True))

print(df.median(numeric_only=True) + df.count(numeric_only=True))

print(df.median(numeric_only=True) + df.idxmax(numeric_only=True))

print(df.median(numeric_only=True) + df.idxmin(numeric_only=True))

print(df.median(numeric_only=True) + df.sum(numeric_only=True))

print(df.median(numeric_only=True) + df.corr(numeric_only=True))

print(df.median(numeric_only=True) + df.describe())

print(df.median(numeric_only=True))
print(df.value_counts())

print(df.median(numeric_only=True) + df.min(numeric_only=True))

print(df.median(numeric_only=True) + df.max(numeric_only=True))

print(df.median(numeric_only=True) + df.std(numeric_only=True))

print(df.median(numeric_only=True) + df.nunique())

print(df.median(numeric_only=True) + df.var(numeric_only=True)) 

print(df.median(numeric_only=True) + df.round())import pandas as pd
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
