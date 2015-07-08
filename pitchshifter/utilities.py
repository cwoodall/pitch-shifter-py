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

def stereoToMono(audio_samples):
    """
    Takes in an 2d array of stereo samples and returns a mono numpy 
    array of dtype np.int16.
    """
    LEFT = 0
    RIGHT = 1
    mono_samples = np.asarray(
        [(sample[RIGHT] + sample[LEFT])/2 for sample in audio_samples], 
        dtype=np.int16
    )

    
    return mono_samples
