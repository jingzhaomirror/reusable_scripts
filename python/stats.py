# -*- coding: utf-8 -*-
"""
@author: jingzhao
"""

import math
from scipy.stats import norm

def find_z(alpha):
    """given significance level alpha, return a corresponding z value
    based on normal distribution, two-tailed"""
    
    return norm.ppf(1-alpha/2)

def find_beta(dmin, se_1, n, alpha):
    """
    given the dmin (minimal value of the absolute practical significant difference),
    se_1 (standard error of the sampling distribution of sample statistics at sample size n=1),
    n (sample size),
    alpha (significance level),
    return the corresponding beta (probability of type II error or 1-power)
    """
    
    z = find_z(alpha)
    se = se_1/math.sqrt(n)
    beta = norm.cdf(se*z, loc=dmin, scale=se)
    return beta
    
def find_samplesize(dmin, se_1, alpha=0.05, beta=0.2, ns=range(1,500000)):
    """
    Given a set of test requirement (alpha, beta, dmin) and standard error, 
    return the minimum sample size required in each group.
    
    Inputs:
    d_min: The practical significance level
    se_1: The standard error of the metric with sample size n=1 in each group,
            if given standard error at size n: se_1 = se_n * sqrt(n)
    alpha: The desired statistical significance level of the test
    beta: The desired beta level (1-power) of the test
    ns: a range of sample sizes to try out
   
    Returns: 
    The smallest n out of the given ns that will achieve the desired beta. 
    If none of the given Ns will work, returns -1.
    note: This is the least required number of samples **in each group** of the experi
ment. For AB testing, the minimium total sample size is 2*n. 
    """
    
    for n in ns:
        cur_beta = find_beta(dmin, se_1, n, alpha)
        if cur_beta <= beta:
            return n
    return -1
    
