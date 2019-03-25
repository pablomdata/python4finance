# ## Object Oriented Programming
import numpy as np
import matplotlib.pyplot as plt

# ### Basics of Python Classes
class ExampleOne(object):
    pass

c = ExampleOne()
c.__str__()
type(c)


class ExampleTwo(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

c = ExampleTwo(1, 'text')
c.a
c.b
c.a = 100
c.a


class Math(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        return self.a + self.b
    def difference(self):
        return self.a-self.b

c = Math(10, 15)
c.addition()
c.difference()

class MoreMath(Math):
    def multiplication(self):
        return self.a * self.b
    def sumproduct(self):
        return self.multiplication()+self.addition()
c = MoreMath(10, 15)


# ### Simple Short Rate Class
def discount_factor(r, t):
    ''' Function to calculate a discount factor.
    
    Parameters
    ==========
    r : float
        positive, constant short rate
    t : float, array of floats
        future date(s), in fraction of years;
        e.g. 0.5 means half a year from now
    
    Returns
    =======
    df : float
        discount factor
    '''
    df = np.exp(-r * t)
      # use of NumPy universal function for vectorization
    return df

# Discount factors for different short rates over 5 years
t = np.linspace(0, 5)
for r in [0.01, 0.05, 0.1]:
    plt.plot(t, discount_factor(r, t), label='r=%4.2f' % r, lw=1.5)
plt.xlabel('years')
plt.ylabel('discount factor')
plt.grid(True)
plt.legend(loc=0)



class ShortRate(object):
    ''' Class to model a constant short rate object.
    
    Parameters
    ==========
    name : string
        name of the object
    rate : float
        positive, constant short rate
    
    Methods
    =======
    get_discount_factors :
        returns discount factors for given list/array
        of dates/times (as year fractions)
    '''
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
    def get_discount_factors(self, time_list):
        ''' time_list : list/array-like '''
        time_list = np.array(time_list)
        return np.exp(-self.rate * time_list)


sr = ShortRate('r', 0.05)

sr.name, sr.rate

time_list = [0.0, 0.5, 1.0, 1.25, 1.75, 2.0]  # in year fractions

sr.get_discount_factors(time_list)

# Discount factors for different short rates over 5 years
for r in [0.025, 0.05, 0.1, 0.15]:
    sr.rate = r
    plt.plot(t, sr.get_discount_factors(t),
             label='r=%4.2f' % sr.rate, lw=1.5)
plt.xlabel('years')
plt.ylabel('discount factor')
plt.grid(True)
plt.legend(loc=0)



# Calculate present values of future cash flows

sr.rate = 0.05
cash_flows = np.array([-100, 50, 75])
time_list = [0.0, 1.0, 2.0]
disc_facts = sr.get_discount_factors(time_list)
disc_facts

# present value list
disc_facts * cash_flows

# net present value
np.sum(disc_facts * cash_flows)

sr.rate = 0.15
np.sum(sr.get_discount_factors(time_list) * cash_flows)

# EXERCISES:
# 1) Make a class that wraps up these computations
# Your class should take as attributes
# a name, time_list, cash_flows, instance of ShortRate class
# and methods to calculate a present value list and the net present value
# 2) Extend your class to analyze the sensitivity to the short rate


# ### SOLUTION: Cash Flow Series Class
#
class CashFlowSeries:
    ''' Class to model a cash flows series.

    Attributes
    ==========
    name : string
        name of the object
    time_list : list/array-like
        list of (positive) year fractions
    cash_flows : list/array-like
        corresponding list of cash flow values
    short_rate : instance of short_rate class
        short rate object used for discounting

    Methods
    =======
    present_value_list :
        returns an array with present values
    net_present_value :
        returns NPV for cash flow series
    '''

    def __init__(self, name, time_list, cash_flows, short_rate):
        self.name = name
        self.time_list = time_list
        self.cash_flows = cash_flows
        self.short_rate = short_rate

    def present_value_list(self):
        df = self.short_rate.get_discount_factors(self.time_list)
        return np.array(self.cash_flows) * df

    def net_present_value(self):
        return np.sum(self.present_value_list())

sr.rate = 0.05
cfs = CashFlowSeries('cfs', time_list, cash_flows, sr)

cfs.cash_flows
cfs.time_list

cfs.present_value_list()

cfs.net_present_value()


class CashFlowSeriesSensitivity(CashFlowSeries):
    def npv_sensitivity(self, short_rates):
        npvs = []
        for rate in short_rates:
            sr.rate = rate
            npvs.append(self.net_present_value())
        return np.array(npvs)


cfs_sens = CashFlowSeriesSensitivity('cfs', time_list, cash_flows, sr)

short_rates = [0.01, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.2]

npvs = cfs_sens.npv_sensitivity(short_rates)
npvs

plt.plot(short_rates, npvs, 'b')
plt.plot(short_rates, npvs, 'ro')
plt.plot((0, max(short_rates)), (0, 0), 'r', lw=2)
plt.grid(True)
plt.xlabel('short rate')
plt.ylabel('net present value')
plt.show()