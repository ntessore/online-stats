ostats
======

Online algorithm for the mean, variance, and covariance.

The `ostats` package contains a single function `ostats.add_sample()` which
updates a sample mean given a new sample, as well as optionally the sample
variance and the sample covariance matrix.

The package has no dependencies, as the `ostats.add_sample()` function works
with any input data type that supports in-place addition and fancy slicing.

Usage
-----

```py
import numpy as np

# the package
import ostats

# online algorithm for the mean
# start from zero
mu = np.zeros(4)

# generate samples and compute their mean
for i in range(1000):
    x = np.random.normal([0.1, 0.3, 0.5, 0.7])
    ostats.add_sample(i, x, mu)

# the mean is computed in place
print(mu)  # [0.08804402 0.25896929 0.44891264 0.73418769]

# compute the variance
mu = np.zeros(4)
var = np.zeros(4)
for i in range(1000):
    x = np.random.normal([0.1, 0.3, 0.5, 0.7], [0.2, 0.4, 0.6, 0.8])
    ostats.add_sample(i, x, mu, var=var)

print(mu)  # [0.09854301 0.29509305 0.4777673  0.70008311]
print(var**0.5)  # [0.19900518 0.4012857  0.59267129 0.81856542]

# compute the covariance matrix
mu = np.zeros(4)
cov = np.zeros((4, 4))
for i in range(100_000):
    x = np.random.multivariate_normal([0.1, 0.3, 0.5, 0.7],
            [[0.2, 0.02, 0.04, 0.06],
             [0.02, 0.4, 0.06, 0.08],
             [0.04, 0.06, 0.6, 0.10],
             [0.06, 0.08, 0.10, 0.8]])
    ostats.add_sample(i, x, mu, cov=cov)

print(mu)  # [0.10095607 0.30486108 0.50113141 0.69912377]
print(cov)
# [[0.20101406 0.02105503 0.0382198  0.06220174]
#  [0.02105503 0.39909545 0.06192678 0.0791239 ]
#  [0.0382198  0.06192678 0.59960537 0.1082596 ]
#  [0.06220174 0.0791239  0.1082596  0.80071002]]

```
