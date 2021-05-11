# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 11:19:30 2021

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

def filtre_passe_bas(x,fc):
    n=len(x)

    fc=1/fc
    inputfpb_data= x
    
    for i in range(1,n):
        x[i]= fc*x[i-1]+inputfpb_data[i]
    x = 1 * x / max(abs(x))

    return x
        
def filtre_passe_haut(x,fc):
    n=len(x)

    fc=-1/fc
    inputfpb_data= x
    
    for i in range(1,n):
        x[i]= fc*x[i-1]+inputfpb_data[i]
    x = 0.99 * x / max(abs(x))

    return x

def filtre_butter_passe_bas(x,fc,fs):
#    fc = 320  # Cut-off frequency of the filter
    
    w = fc / (fs / 1) # Normalize the frequency
    b, a = signal.butter(1, w, 'low')
    y = signal.filtfilt(b, a, x)
    y = 0.99 * y / max(abs(x))

    return y

def filtre_butter_passe_haut(x,fc,fs):
    
#    fc = 1160  # Cut-off frequency of the filter
    
    w = fc / (fs / 2) # Normalize the frequency
    b, a = signal.butter(1, w, 'highpass')
    y = signal.filtfilt(b, a, x)
    y = 0.99 * y / max(abs(y))

    return y