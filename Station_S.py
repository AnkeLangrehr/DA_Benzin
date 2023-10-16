import pandas as pd

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

# Erstes Element setzen
station = dfStations.iloc[0]

print("First Element:")
print(station)


# Welches ist die südlichste Tankstelle Deutschlands?

station = dfStations[dfStations['latitude'] == dfStations['latitude'].min()]

print("Südlichste Station:")
for index, s in station.iterrows():
    print(s)
