# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 11:01:08 2021

@author: duwat
"""
import numpy as np
import scipy.io.wavfile as wavfile
from scipy.signal import lfilter
from scipy.signal import butter,filtfilt
from scipy import signal
import soundfile
from scipy.fftpack import fft2, ifft2
import matplotlib.pyplot as plt
import math
import cmath


def disto(x,d):
    n=len(x)
    for i in range (n):
        k=x[i]
        j=np.absolute(k)
        if d==0:
            x[i]=x[i]
        elif k==0:
            x[i]=0
        else:
            x[i]=(k/j)*(1-np.exp(-(d*(k**2))/j))
    x = 0.99 * x / max(abs(x))

    return x


