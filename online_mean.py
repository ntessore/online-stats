# author: Nicolas Tessore <n.tessore@ucl.ac.uk>
# license: MIT
'''online algorithm for mean, variance, and covariance'''

__version__ = '2023.1'

import numpy as np


def add_sample(n, x, mu, *, var=None, cov=None):
    '''add sample to online statistics'''
    delta = x - mu
    mu += delta/(n+1)
    if var is not None:
        var += (delta*(x - mu) - var)/(n+1)
    if cov is not None:
        cov += (np.outer(delta, x - mu) - cov)/(n+1)
