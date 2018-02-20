import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')
# df = data frame
dataf = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

dataf['100ma'] = dataf['Close'].rolling(window=100,min_periods=0).mean() #mean() é media
# dataf.dropna(inplace=True)

print(dataf.tail())

ax1 = plt.subplot2grid((6,1),(0,0),rowspan = 5, colspan=1)
ax2 = plt.subplot2grid((6,1),(5,0),rowspan = 1, colspan=1, sharex=ax1)

ax1.plot(dataf.index, dataf['Close'])
ax1.plot(dataf.index, dataf['100ma'])
ax2.bar(dataf.index, dataf['Volume'])

plt.show()
