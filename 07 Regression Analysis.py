# ## Regression Analysis
# Relation between SP500 and VIX (volatility index exchange market)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# data from Thomson Reuters Eikon API
raw = pd.read_csv('./python4finance/data/tr_eikon_eod_data.csv',
                  index_col=0, parse_dates=True)
spx = pd.DataFrame(raw['.SPX'])

np.round(spx.tail())

vix = pd.DataFrame(raw['.VIX'])
vix.info()

data = spx.join(vix)
data.tail()

data.plot(subplots=True, grid=True, style='b', figsize=(8, 6))

rets = np.log(data / data.shift(1))
rets.head()
rets.dropna(inplace=True)

rets.plot(subplots=True, grid=True, style='b', figsize=(8, 6))

x = rets['.SPX'].values
y = rets['.VIX'].values
reg = np.polyfit(x=x, y=y, deg=1)
reg

plt.plot(x, y, 'r.')
ax = plt.axis()  # grab axis values to plot regression line
x = np.linspace(ax[0], ax[1] + 0.01)
plt.plot(x, np.polyval(reg, x), 'b', lw=2)
plt.grid(True)
plt.axis('tight')
plt.xlabel('S&P 500 returns')
plt.ylabel('VIX returns')

rets.corr()

rets['.SPX'].rolling(window=252).corr(rets['.VIX']).plot(grid=True, style='b')
