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
#pd.to_datetime(
dfPrices['time'] = pd.to_datetime(dfPrices['date'])
date = []

# for index, s in dfPrices.iterrows():
#     yData.append(s['diesel'])
#     xData.append(s["e10"])
#     zData.append(s["e5"])

# plt.scatter(date,yData)
for col in ['diesel', 'e10', 'e5']:
    time = dfPrices['time']
    timeConv = pd.to_datetime(time).dt.time
    plt.xlabel=timeConv
    plt.plot(timeConv, dfPrices[col])

plt.show()
