import pandas as pd

# Wo gab es vorgestern den günstigsten Diesel?

#Preise laden
dfFull = pd.read_csv(r'data\prices\2023\10\2023-10-11-prices.csv')

dfPrices = pd.DataFrame(dfFull)
print(dfPrices.head())
print(dfPrices.columns)
print(dfPrices.dtypes)

#Aufräumen
dfPrices = dfPrices.drop(dfPrices[dfPrices['diesel'] <= 0].index, inplace=False)
dfPrices.dropna()
dfPrices.dropna(inplace=False)

# Erstes Element setzen
price = dfPrices.iloc[0]


#Laden aller Stations
path = r'data\stations\2023\10\2023-10-12-stations.csv'

dfs = pd.read_csv(path)

dfStations = pd.DataFrame(dfs)
print(dfStations.head())
print(dfStations.columns)
print(dfStations.dtypes)

# clean Data
dfStations = dfStations.drop(dfStations[dfStations['name'] == 'please delete - bitte loeschen'].index, inplace=False)
dfStations = dfStations.drop(dfStations[dfStations['latitude'] == 0.0].index, inplace=False)
dfStations = dfStations.drop(dfStations[dfStations['longitude'] == 0.0].index, inplace=False)


print("First Element:")
print(price)
print(dfStations.columns)


print("Günstigester Diesel:")
price = dfPrices[dfPrices['diesel'] == dfPrices['diesel'].min()]

for index, p in price.iterrows():
    print(p)
    stations = dfStations[dfStations['uuid']==p['station_uuid']]

for index, s in stations.iterrows():
    print(s)