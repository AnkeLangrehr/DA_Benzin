import pandas as pd
import glob
from pathlib import Path
import pyarrow


filesFull = glob.glob('C:/Users/ankel/Documents/Projekte/SVA_Benzin/data/prices/2022/*/*.csv',
                       recursive=True)

dfFilesFull = []

for file in filesFull:
    print(file)
    content = pd.read_csv(file, engine="pyarrow", usecols=['e10', 'station_uuid'])
    dfFilesFull.append(content)

df_prices_2022 = pd.concat(dfFilesFull, ignore_index=True)
print(df_prices_2022.columns)



idx = df_prices_2022.index[df_prices_2022['e10'] <= 0.0]
df_prices_2022 = df_prices_2022[~df_prices_2022.index.isin(idx)]

# idx = df_prices_2022.index[df_prices_2022['e10'] >= 4.0]
# df_prices_2022 = df_prices_2022[~df_prices_2022.index.isin(idx)]

price = df_prices_2022[df_prices_2022['e10'] == df_prices_2022['e10'].max()]

for index, p in price.iterrows():
    print(p)