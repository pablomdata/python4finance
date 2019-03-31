# ## Implied Volatilities
import datetime as dt
import pandas as pd
import time

# Iterate over rows:
def naive_iterate(data):
    start = time.time()
    for ix in data.index:
        data.loc[ix, 'DATE'] = dt.date.fromtimestamp(data.loc[ix, 'DATE']/1e9)
    end = time.time()
    print("It took: ", end-start)


# Fancy iterate
def fancy_iterate(data):
    start = time.time()
    for ix, row in data.iterrows():
        data.loc[ix, 'DATE'] = dt.date.fromtimestamp(row['DATE']/1e9)
    end = time.time()
    print("It took: ", end-start)


# Using apply
def use_apply(data):
    start = time.time()
    data['DATE'] = data['DATE'].apply(lambda row: dt.date.fromtimestamp(row / 1e9))
    end = time.time()
    print("It took: ", end-start)

if __name__ == "__main__":
    h5 = pd.HDFStore('../data/vstoxx_data_31032014.h5', 'r')
    futures_data = h5['futures_data']  # VSTOXX futures data to see moneyness
    h5.close()

    naive_iterate(futures_data.copy())
    fancy_iterate(futures_data.copy())
    use_apply(futures_data.copy())    