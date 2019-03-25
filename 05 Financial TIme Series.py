
import matplotlib.pyplot as plt

# ## pandas Basics

import numpy as np
import pandas as pd

# First Steps with DataFrame Class
df = pd.DataFrame([10, 20, 30, 40], columns=['numbers'],
                  index=['a', 'b', 'c', 'd'])
df


df.index  # the index values

df.columns  # the column names

df.loc['c']  # selection via index

df.loc[['a', 'd']]  # selection of multiple indices

df.loc[df.index[1:3]]  # selection via Index object


df.sum()  # sum per column


df.apply(lambda x: x ** 2)  # square of every element


df ** 2  # again square, this time NumPy-like

df['floats'] = (1.5, 2.5, 3.5, 4.5) # new column is generated

df['floats']  # selection of column

df['names'] = pd.DataFrame(['Yves', 'Guido', 'Felix', 'Francesc'],
                           index=['d', 'a', 'b', 'c'])


df.append({'numbers': 100, 'floats': 5.75, 'names': 'Henry'}, ignore_index=True)
# temporary object; df not changed

# to pass a value with an index, we need to convert the record to a 1-row data frame
df = df.append(
                pd.DataFrame({'numbers': 100, 'floats': 5.75,
                             'names': 'Henry'}, index=['z',])
    )


other_df = pd.DataFrame([1, 4, 9, 16, 25],
            index=['a', 'b', 'c', 'd', 'y'],
            columns=['squares',])


df.join(other_df)
df.join(other_df, how='left')
df.join(other_df, how='right')
df.join(other_df, how='outer')

df[['numbers', 'squares']].mean()
  # column-wise mean

df[['numbers', 'squares']].std()
  # column-wise standard deviation


# ### Second Steps with DataFrame Class

a = np.random.standard_normal((9, 4))
a.round(6)

df = pd.DataFrame(a)
df

df.columns = ['No1', 'No2', 'No3', 'No4']
df

df['No2'].iloc[3]


dates = pd.date_range('2015-1-1', periods=9, freq='M')
dates

df.index = dates
df

# ### Basic Analytics

df.sum()
df.sum(axis=1)

df.mean()

df.cumsum()

df.describe()

np.sqrt(abs(df))

np.sqrt(abs(df)).sum()

df.hist()
df.boxplot()

df.cumsum().plot(grid=True)
df.cumsum().plot()

plt.ioff()
df.cumsum().plot()
plt.savefig("./python4finance/data/chart.png")


df.hist()
plt.show()


# ### Series Class

type(df)

df['No1']

type(df['No1'])

df['No1'].cumsum().plot(style='r', lw=2., grid=True)
plt.xlabel('date')
plt.ylabel('value')
plt.title("Running sum")
plt.show()

# ### GroupBy Operations
df['Quarter'] = ['Q1', 'Q1', 'Q1', 'Q2', 'Q2', 'Q2', 'Q3', 'Q3', 'Q3']
df

df.boxplot(by='Quarter')

groups = df.groupby('Quarter')

groups.mean()

groups.max()

groups.size()

# Grouping by two keys
df['Odd_Even'] = ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even',
                  'Odd', 'Even', 'Odd']

groups = df.groupby(['Quarter', 'Odd_Even'])

groups.size()

groups.mean()
