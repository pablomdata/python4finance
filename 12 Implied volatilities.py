# ## Implied Volatilities
import datetime as dt
import pandas as pd
from python4finance.bsm_functions import *
import matplotlib.pyplot as plt

V0 = 17.6639 # Value of VSTOXX index on March 21, 2014

r = 0.01 # risk-free short rate, p.a.


h5 = pd.HDFStore('./python4finance/data/vstoxx_data_31032014.h5', 'r')
futures_data = h5['futures_data']  # VSTOXX futures data to see moneyness
options_data = h5['options_data']  # VSTOXX call option data
h5.close()

# Reformat the dates to use in pandas
futures_data['DATE'] = futures_data['DATE'].apply(lambda x: dt.date.fromtimestamp(x / 1e9))
futures_data['MATURITY'] = futures_data['MATURITY'].apply(lambda x: dt.date.fromtimestamp(x / 1e9))
futures_data

# Options data is larger, since multiple call and put options are traded at the same maturity date
options_data['DATE'] = options_data['DATE'].apply(lambda x: dt.date.fromtimestamp(x / 1e9))
options_data['MATURITY'] = options_data['MATURITY'].apply(lambda x: dt.date.fromtimestamp(x / 1e9))
options_data.info()
options_data[['DATE', 'MATURITY', 'TTM', 'STRIKE', 'PRICE']].head()

options_data['IMP_VOL'] = 0.0 # new column for implied volatilities


tol = 0.5  # tolerance level for moneyness
for option in options_data.index:
    # iterating over all option quotes
    mask = futures_data['MATURITY'] == options_data.loc[option]['MATURITY']
    forward = futures_data[mask]['PRICE'].values[0] # picking the right futures value
    strike = options_data.loc[option]['STRIKE']
    if forward * (1 - tol) < strike < forward * (1 + tol):
        # only for options with moneyness within tolerance
        imp_vol = bsm_call_imp_vol(
                V0,  # VSTOXX value
                options_data.loc[option]['STRIKE'],
                options_data.loc[option]['TTM'],
                r,   # short rate
                options_data.loc[option]['PRICE'],
                sigma_est=2.,  # estimate for implied volatility
                it=100)
        options_data.loc[option, 'IMP_VOL'] = imp_vol

plot_data = options_data[options_data['IMP_VOL'] > 0]


maturities = sorted(set(options_data['MATURITY']))
maturities


# Implied volatilities (of volatility) for European call options on the VSTOXX on 31. March 2014
plt.figure(figsize=(8, 6))
for maturity in maturities:
    data = plot_data[options_data.MATURITY == maturity]
      # select data for this maturity
    plt.plot(data['STRIKE'], data['IMP_VOL'],
             label=maturity, lw=1.5)
    plt.plot(data['STRIKE'], data['IMP_VOL'], 'r.', label='')
plt.grid(True)
plt.xlabel('strike')
plt.ylabel('implied volatility of volatility')
plt.legend()

# Smile / maturity?

group_data = plot_data.groupby(['MATURITY', 'STRIKE'])[['PRICE', 'IMP_VOL']]
group_data

group_data = group_data.sum()
group_data.head()
