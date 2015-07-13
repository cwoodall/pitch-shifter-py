#!python

import numpy as np
from scipy.interpolate import interp1d

def linear_resample(samples, out_len):
    """
    Resamples samples to have length equal to out_len.

    Uses a 1d linear interpolator
    
    Args:
      samples: samples to resample using an interpolator
      out_len: Length of output sample size. 
    
    Returns:
        resampled and interpolated output.
    """
    sample_size = len(samples)
    interpolator = interp1d(np.arange(0, sample_size), samples, kind='linear')
    
    resample_n = np.linspace(0, sample_size-1, out_len)
    return interpolator(resample_n)
    
