import pandas as pd
import matplotlib.pyplot as plt
import datetime
from datetime import datetime

dfFull = pd.read_csv(r'data\prices\2023\10\2023-10-11-prices.csv')

dfPrices = pd.DataFrame(dfFull)
print(dfPrices.head())
print(dfPrices.columns)
print(dfPrices.dtypes)

xData = []
yData = []
zData = []

dfPrices["time"] = pd.to_datetime(dfPrices["date"])
dfPrices["time"] = dfPrices["time"].dt.strftime('%H:%M')
date = []

plt.hist( dfPrices["e10"] )
plt.title("E10 1. Stand")
plt.show()


dfPrices = dfPrices.drop(dfPrices[dfPrices['diesel'] <= 1.0].index, inplace=False)
dfPrices = dfPrices.drop(dfPrices[dfPrices['e10'] <= 1.0].index, inplace=False)
dfPrices = dfPrices.drop(dfPrices[dfPrices['e5'] <= 1.0].index, inplace=False)

plt.hist( dfPrices["e10"] )
plt.title("E10 2.Stand")
plt.show()


dfPrices = dfPrices.drop(dfPrices[dfPrices['diesel'] >= 5.0].index, inplace=False)
dfPrices = dfPrices.drop(dfPrices[dfPrices['e10'] >= 5.0].index, inplace=False)
dfPrices = dfPrices.drop(dfPrices[dfPrices['e5'] >= 5.0].index, inplace=False)
dfPrices.dropna()

plt.hist( dfPrices["e10"] )
plt.title("E10 3.Stand")
plt.show()
