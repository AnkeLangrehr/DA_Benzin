import pandas as pd
import glob
import os
import numpy as np
import csv
from pathlib import Path

path = r'data\stations\2023\10\2023-10-12-stations.csv'

# Get the files from the path provided in the OP
# csv_files = Path(path).rglob('*.csv',
#    index_col=0,
# )  # .rglob to get subdirectories

dfs = pd.read_csv(path,
                  index_col=0, )

dfStations = pd.DataFrame(dfs)
print(dfStations.head())
print(dfStations.columns)
print(dfStations.dtypes)

# clean Data
dfStations = dfStations.drop(dfStations[dfStations['name'] == 'please delete - bitte loeschen'].index, inplace=False)
dfStations = dfStations.drop(dfStations[dfStations['latitude'] == 0.0].index, inplace=False)
dfStations = dfStations.drop(dfStations[dfStations['longitude'] == 0.0].index, inplace=False)

# Erstes Element setzen
station = dfStations.iloc[0]

print("First Element:")
print(station)


# Welches ist die südlichste Tankstelle Deutschlands?

station = dfStations[dfStations['latitude'] == dfStations['latitude'].min()]

print("Südlichste Station:")
for index, s in station.iterrows():
    print(s)



# Wo gab es vorgestern den günstigsten Diesel?

dfFull = pd.read_csv(r'data\prices\2023\10\2023-10-11-prices.csv')

dfPrices = pd.DataFrame(dfFull)
print(dfPrices.head())
print(dfPrices.columns)
print(dfPrices.dtypes)

dfPrices = dfPrices.drop(dfPrices[dfPrices['diesel'] <= 0].index, inplace=False)
dfPrices.dropna()
dfPrices.dropna(inplace=False)

# Erstes Element setzen
price = dfPrices.iloc[0]

print("First Element:")
print(price)

print("Günstigester Diesel:")
price = dfPrices[dfPrices['diesel'] == dfPrices['diesel'].min()]

for index, p in price.iterrows():
    print(p)
