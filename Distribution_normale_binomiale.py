# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 15:45:15 2021

@author: Zakaria
"""

import matplotlib.pyplot as plt
import numpy as np

"""
# X = Z * O + µ

mu = 0.6
sigma = 0.2

dtst = np.random.normal(mu, sigma, 10000)

count, bins, ignored = plt.hist(dtst, bins=20, color="lightblue")

plt.plot(bins, 1/(sigma * np.sqrt(2*np.pi)) * np.exp(-(bins - mu)**2 / (2 * sigma**2)),linewidth=3, color='r')

plt.show()
"""

n = 10
p = 0.5

data_binom = np.random.binomial(n, p, 10000)

answer = sum(np.random.binomial(9, 0.1, 20000)==0)/20000

print(answer)