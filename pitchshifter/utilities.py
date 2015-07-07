#!python

import numpy as np
import scipy as sp

def complex_polarToCartesian(r, theta):
    """
    Convert a polar representaiton of a complex number to a cartesian
    representation.

    Can be used with a numpy array allowing for block conversions
    """
    return r * np.exp(theta*1j)

