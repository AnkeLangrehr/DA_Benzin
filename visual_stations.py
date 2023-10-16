from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset:
path = r'data\stations\2023\10\2023-10-12-stations.csv'

dfs = pd.read_csv(path,
                  index_col=0, )
dfStations = pd.DataFrame(dfs)

# visuelle Analyse

xData = []
yData = []
print(dfStations.columns)
for index, s in dfStations.iterrows():
    yData.append(s['latitude'])
    xData.append(s["longitude"])

plt.scatter(x=xData, y=yData)
plt.show()

# 1.Bereinigung

dfStations = dfStations.drop(dfStations[dfStations['name'] == 'please delete - bitte loeschen'].index, inplace=False)
dfStations = dfStations.drop(dfStations[dfStations['latitude'] == 0.0].index, inplace=False)
dfStations = dfStations.drop(dfStations[dfStations['longitude'] == 0.0].index, inplace=False)
dfStations.dropna()

xData = []
yData = []

print(dfStations.columns)
for index, s in dfStations.iterrows():
    yData.append(s['latitude'])
    xData.append(s["longitude"])

plt.scatter(x=xData, y=yData)
plt.show()
# daten zeigen Ausreißer, die sinnfrei sind
# Daten weiter bereinigen!
dfStations = dfStations.drop(dfStations[dfStations['latitude'] >= 57.0].index, inplace=False)
dfStations = dfStations.drop(dfStations[dfStations['longitude'] >= 16.0].index, inplace=False)

xData = []
yData = []
print(dfStations.columns)
for index, s in dfStations.iterrows():
    yData.append(s['latitude'])
    xData.append(s["longitude"])

plt.scatter(x=xData, y=yData)
plt.show()

# #Daten passen. Abfahrt!
# Hier folgt K-Means
# data = list(zip(xData, yData))
#
# inertias = []
#
# for i in range(1,20):
#     kmeans = KMeans(n_clusters=i)
#     kmeans.fit(data)
#     inertias.append(kmeans.inertia_)
#
# plt.plot(range(1,20), inertias, marker='o')
# plt.title('Elbow method')
# plt.xlabel('Number of clusters')
# plt.ylabel('Inertia')
# plt.show()
#
#
# kmeans = KMeans(n_clusters=3)
# kmeans.fit(data)
#
# plt.scatter(xData, yData, c=kmeans.labels_)
# plt.show()
#
# kmeans = KMeans(n_clusters=4)
# kmeans.fit(data)
#
# plt.scatter(xData, yData, c=kmeans.labels_)
# plt.show()
#
# kmeans = KMeans(n_clusters=5)
# kmeans.fit(data)
#
# plt.scatter(xData, yData, c=kmeans.labels_)
# plt.show()

