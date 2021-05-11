# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 11:15:26 2021

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

def tremolo(x,ftr,r,fs):
#    ftr=4
#    r=0.5
    n=len(x)
    for i in range(n):
        x[i]=x[i]+r*x[i]*np.sin(2*np.pi*ftr*i/fs)
    x = 0.99 * x / max(abs(x))
    return x
    

def delay(x,a,d):
#    a=0.5
#    d=5000
    n=len(x)
    input_data_delay=x
    for i in range(d,n) :
      x[i]=a*x[i-d]+ input_data_delay[i]
      x = 0.99 * x / max(abs(x))

    return x
  
  
def reverb(x,a,fs):
    n=len(x)
#    a=0.5
    y=x
        
#    d=int(2*fs*0.2)
    d=4000
    
    
    
    for i in range(d,n) :
        y[i]= a*y[i-d] + x[i]
    print(max(y))
    y = 0.99 * y / max(abs(y))

    return y