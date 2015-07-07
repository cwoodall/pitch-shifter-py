#!python

import numpy as np
import scipy as sp

def stft(x, fs, chunk_size, hop):
    """
    SHORT TIME FOURIER TRANSFORM...
    """
    w = sp.hamming(chunk_size)
    X = sp.array([sp.fft(w*x[i:i+chunk_size])
                     for i in range(0, len(x)-chunk_size, hop)])/np.sqrt(((chunk_size/hop)/2))
    return X

def istft(X, fs, chunk_size, hop):
    x = sp.zeros(len(X) * (hop))
    w = sp.hamming(chunk_size)
    i_p = 0
    for n, i in enumerate(range(0, len(x)-chunk_size, hop)):
        x[i:i+chunk_size] += w*sp.real(sp.ifft(X[n]))
    return x
