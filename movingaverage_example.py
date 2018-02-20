import datetime as dt
import matplotlib as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')
# df = data frame
dataf = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

dataf['100ma']
