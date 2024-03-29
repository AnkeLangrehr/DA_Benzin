import pandas as pd
import glob
from pathlib import Path

# Wie hoch war 2022 der höchste Preis für E10?
dfFiles = []

filesMonth = glob.glob('C:/Users/ankel/Documents/Projekte/SVA_Benzin/data/prices/2022/12/*.csv',
                       recursive=True)
for file in filesMonth:
    content = pd.read_csv(file, usecols=[1, 4])
    dfFiles.append(content)

df_prices_12_2022 = pd.concat(dfFiles)
print(df_prices_12_2022.columns)
print(df_prices_12_2022.columns.dtype)

#Drop mit Pandas - sehr langsam:
# df_prices_12_2022.drop(df_prices_12_2022[df_prices_12_2022['e10'] <= 0.0].index, inplace=True)
# df_prices_12_2022.drop(df_prices_12_2022[df_prices_12_2022['e10'] >= 4.0].index, inplace=True)
# df_prices_12_2022.dropna(inplace=False)

#Bessere Möglichkeit: Daten invertieren mit ~
idx = df_prices_12_2022.index[df_prices_12_2022['e10'] <= 0.0]
df_prices_12_2022 = df_prices_12_2022[~df_prices_12_2022.index.isin(idx)]

#Obere Beschränkung der Daten?
#idx = df_prices_12_2022.index[df_prices_12_2022['e10'] >= 4.0]
#df_prices_12_2022 = df_prices_12_2022[~df_prices_12_2022.index.isin(idx)]

print(df_prices_12_2022.head())

# Erstes Element setzen
price = df_prices_12_2022.iloc[0]

print("First Element:")
print(price)

print("Höchster Preis für E10 in 12.2022:")
price = df_prices_12_2022[df_prices_12_2022['e10'] == df_prices_12_2022['e10'].max()]

for index, p in price.iterrows():
    print(p)

