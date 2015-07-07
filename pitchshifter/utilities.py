#!python

import numpy as np
import scipy as sp

def complex_polarToCartesian(r, theta):
    """
    Convert a polar representaiton of a complex number to a cartesian
    representation.

    Can be used with a numpy array allowing for block conversions

    Example Usage:         
    
    results = complex_polarToCartesian(1.4142, 0.7854)

    results approx. 1+1j 
    """
    return r * np.exp(theta*1j)

def complex_cartesianToPolar(x):
    """
    Convert a cartesian representaiton of a complex number to a polar
    representation.

    Can be used with a numpy array allowing for block conversions

    Example Usage:         
    
    results = complex_cartesianToPolar(1 + 1j)

    results approx. (1.4142, 0.7854)
    """
    return (np.abs(x), np.angle(x))
