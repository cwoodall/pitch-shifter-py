#!python

import numpy as np
import scipy as sp

def stft(x, chunk_size, hop, w=None):
    """
    Takes the short time fourier transform of x.

    Args:
      x: samples to window and transform.
      chunk_size: size of analysis window.
      hop: hop distance between analysis windows
      w: windowing function to apply. Must be of length chunk_size

    Returns:
      STFT of x (X(t, omega)) hop size apart with windows of size chunk_size.

    Raises:
      ValueError if window w is not of size chunk_size
    """
    if not w:
        w = sp.hanning(chunk_size)
    else:
        if len(w) != chunk_size:
            raise ValueError("window w is not of the correct length {0}.".format(chunk_size))
    X = sp.array([sp.fft(w*x[i:i+chunk_size])
                     for i in range(0, len(x)-chunk_size, hop)])/np.sqrt(((float(chunk_size)/float(hop))/2.0))
    return X

def istft(X, chunk_size, hop, w=None):
    """
    Naively inverts the short time fourier transform using an overlap and add
    method. The overlap is defined by hop

    Args:
      X: STFT windows to invert, overlap and add. 
      chunk_size: size of analysis window.
      hop: hop distance between analysis windows
      w: windowing function to apply. Must be of length chunk_size

    Returns:
      ISTFT of X using an overlap and add method. Windowing used to smooth.

    Raises:
      ValueError if window w is not of size chunk_size
    """

    if not w:
        w = sp.hanning(chunk_size)
    else:
        if len(w) != chunk_size:
            raise ValueError("window w is not of the correct length {0}.".format(chunk_size))

    x = sp.zeros(len(X) * (hop))
    i_p = 0
    for n, i in enumerate(range(0, len(x)-chunk_size, hop)):
        x[i:i+chunk_size] += w*sp.real(sp.ifft(X[n]))
    return x
