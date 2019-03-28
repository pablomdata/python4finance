
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

raw = pd.read_csv('../data/tr_eikon_eod_data.csv',
                   index_col=0, parse_dates=True)

start_date = '2010-01-05'
end_date = '2010-01-08'
raw[start_date:end_date]


AAPL = pd.DataFrame(raw['AAPL.O'])
AAPL.columns = ['Close']
AAPL.info()

# Historical levels of AAPL

AAPL['Close'].plot(grid=True, figsize=(8, 5))

AAPL['42d'] = np.round(AAPL['Close'].rolling(window=42).mean(), 2)
AAPL['252d'] = np.round(AAPL['Close'].rolling(window=252).mean(), 2)

AAPL[['Close', '42d', '252d']].tail()

AAPL[['Close', '42d', '252d']].plot(grid=True, figsize=(8, 5))
# tag: AAPL_trend
# title: The Apple, Inc. stock price with 42d and 252d trend lines

AAPL['42-252'] = AAPL['42d'] - AAPL['252d']
AAPL['42-252'].tail()


AAPL['42-252'].head()


AAPL.dropna(inplace=True)


SD = 0.5
AAPL['Position'] = np.where(AAPL['42-252'] > SD, 1, 0)
AAPL['Position'] = np.where(AAPL['42-252'] < -SD, -1, AAPL['Position'])
AAPL['Position'].value_counts()


AAPL['Position'].plot(lw=1.5, grid=True)
plt.ylim([-1.1, 1.1]);

AAPL['Market'] = np.log(AAPL['Close'] / AAPL['Close'].shift(1))
AAPL['Strategy'] = AAPL['Position'].shift(1) * AAPL['Market']
AAPL[['Market', 'Strategy']].cumsum().apply(np.exp).plot(grid=True,
                                                         figsize=(8, 5))

# The Apple stock performance vs. investor's wealth