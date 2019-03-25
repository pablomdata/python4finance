# ## High Frequency Data
import pandas as pd

# data from FXCM Forex Capital Markets Ltd.
eur_usd = pd.read_csv('./python4finance/data/fxcm_eur_usd_tick_data.csv',
                      index_col=0, parse_dates=True)
eur_usd.info()

eur_usd['Avg'] = eur_usd.mean(axis=1)

eur_usd['Avg'].plot(figsize=(10, 6), title="EUR/USD tick data for two hours")

eur_usd_3min = eur_usd.resample('3T').sum() #Downsample the series to 3 minute bins and sum the values in a bin
eur_usd.resample('0.5S').last().head() # number+S/T/H/W/M
eur_usd.head(100)

# http://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html
eur_usd_3min.head()
eur_usd_3min.resample('T').bfill().head() #bfill and ffill