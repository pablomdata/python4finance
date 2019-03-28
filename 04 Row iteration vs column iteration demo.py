from timeit import timeit

setup = """
import numpy as np
a = np.arange(100000000).reshape(10000, 10000)

def contiguous_sum(x):
	for i in range(x.shape[0]):
		x[i].sum()

def non_contiguous_sum(x):
	for i in range(x.shape[-1]):
		x[:, i].sum()
"""
n=100
time_contiguous = timeit('contiguous_sum(a)', setup=setup, number=n) / n
time_non_contiguous = timeit('non_contiguous_sum(a)', setup=setup, number=n) / n
print("Contiguous: {:.4f}s per loop".format(time_contiguous))
print("Non-contiguous: {:.4f}s per loop".format(time_non_contiguous))