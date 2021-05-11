# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 11:03:22 2021

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




def flanger(x,A,rate,manual,l,fs):
    data_flanger=x

#    A = 50
#    l=1
#    rate = 0.2
#    manual = 10
    period = 1/fs
    
    p=int(len(x)-A-manual)
    
    for i in range (p):
        
        t=int(A*np.sin(2*np.pi*i*rate*period))
        
        x[i] = x[i] + l*data_flanger[(i + manual + t)]
    
    x = 0.99 * x / max(abs(x))
    return x
   
    
    
def chorus(x,A1,A2,A3,rate1,rate2,rate3,manual,l1,l2,l3,fs):
    y=flanger(x,A1,rate1,manual,l1,fs)
    z=flanger(y,A2,rate2,manual,l2,fs)
    o=flanger(z,A3,rate3,manual,l3,fs)
    return o