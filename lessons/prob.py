from scipy.stats import binom
import numpy as np

def dbinom(x,size,prob=0.5):
    """
    Calculates the point estimate of the binomial distribution
    """
    #from scipy.stats import binom
    result=binom.pmf(k=x,n=size,p=prob,loc=0)
    return result

x = dbinom(2,100,0.2)
print(x)