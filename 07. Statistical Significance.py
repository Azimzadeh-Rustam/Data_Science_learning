from scipy.stats import t
from math import sqrt
import pandas as pd

# sample size
n = 10

# Calculating the critical value from a T-distribution with a 95% critical value range
lower_cv = t(n-1).ppf(.025)
upper_cv = t(n-1).ppf(.975)

# correlation coefficient (from example 06)
r = 0.957586

# Perform the test
test_value = r / sqrt((1-r**2) / (n-2))

print(f"TEST VALUE: {test_value}")
print(f"CRITICAL RANGE: {lower_cv}, {upper_cv}")

if test_value < lower_cv or test_value > upper_cv:
    print("CORRELATION PROVEN, REJECT H0")
else:
    print("CORRELATION NOT PROVEN, FAILED TO REJECT H0 ")

# Calculate p-value
if test_value > 0:
    p_value = 1.0 - t(n-1).cdf(test_value)
else:
    p_value = t(n-1).cdf(test_value)

# Two-tailed, so multiply by 2
p_value = p_value * 2
print(f"P-VALUE: {p_value}")
