import numpy as np
import scipy.stats as st
import scipy.special as sp
n = 100 # number of coin flips
h = 61  # number of heads
q = .5  # null-hypothesis of fair coin

#Get the z score
xbar = float(h)/n
z = (xbar - q) * np.sqrt(n / (q*(1-q))); z


#Get the p val
pval = 2 * (1 - st.norm.cdf(z)); pval
