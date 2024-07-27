# implementing the black sholes formula in Python
import numpy as np
from scipy.stats import norm

#define variables
r=0.01
S= 30
K = 40
T = 240/365
sigma = 0.30

def blacksholes(r, S, K, T, sigma, type="C"):
    "Calculate BS option price for a call/put"
    d1 = (np.log(S/k)+(r+sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        if type == "C":
            price = S*norm.cdf(d1, 0, 1) 